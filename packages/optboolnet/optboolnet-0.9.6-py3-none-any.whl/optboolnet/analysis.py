from typing import Any, List
from optboolnet.log import EnumBendersStep, EnumCutType, BendersLogger
from optboolnet.instances import iter_bn_in_repo
import pandas as pd

_build_log_columns = ["log_level"] + BendersLogger.build_log_columns
_solve_log_columns = ["log_level"] + BendersLogger.solve_log_columns
_cut_log_columns = ["log_level"] + BendersLogger.cut_log_columns
inst_list = ["S1", "S2", "S3", "S4", "M1", "M2", "M3", "L1", "L2", "L3", "L4"]


class BendersAnalysis:
    def __init__(
        self,
        build_log_fname: str,
        solve_log_fname: str,
        cut_log_fname: str,
        option_names: List[str],
        options: List[Any],
        inst: str,
    ) -> None:
        self.option_names = option_names
        self.options = options
        self.inst = inst
        self.build_log = self.rename_exp(pd.read_csv(build_log_fname))
        self.solve_log = self.rename_exp(pd.read_csv(solve_log_fname))
        self.solve_log["model"] = (
            self.solve_log["model"].str.replace("'", "").astype(pd.Int64Dtype())
        )
        self.cut_log = self.rename_exp(pd.read_csv(cut_log_fname))

    @property
    def key_list(self):
        return self.option_names + ["inst"]

    @property
    def key_len(self):
        return len(self.key_list)

    def rename_exp(self, df: pd.DataFrame):
        df.drop(columns=["experiment"], inplace=True)
        df["inst"] = self.inst
        for opt_name, opt in zip(self.option_names, self.options):
            df[opt_name] = opt
        return df

    @property
    def solution_count(self):
        return (
            self.cut_log.loc[
                self.cut_log["cut_type"] == EnumCutType.MINIMALITY.name,
                self.key_list + ["level", "cut_strength"],
            ]
            .groupby(self.key_list + ["level"])
            .count()
            .rename(columns={"cut_strength": "sol"})
            .reset_index()
        )

    @property
    def build_time(self):
        return (
            self.build_log[self.key_list + ["timestamp"]]
            .groupby(self.key_list)
            .max()
            .rename(columns={"timestamp": "build_time"})
            .reset_index()
        )

    @property
    def completion_time(self):
        return (
            self.solve_log[self.key_list + ["level", "timestamp"]]
            .groupby(self.key_list + ["level"])
            .max()
            .rename(columns={"timestamp": "completion_time"})
            .reset_index()
        )

    @property
    def computation_time(self):
        return (
            self.solve_log.loc[
                self.solve_log["step"] != EnumBendersStep.FINISHED.name,
                self.key_list + ["step", "solve_time"],
            ]
            .groupby(self.key_list + ["step"])
            .sum()
            .rename(columns={"timestamp": "completion_time"})
            .reset_index()
        )

    @property
    def count_cuts(self):
        return (
            self.cut_log.loc[
                self.cut_log["cut_type"] != EnumCutType.MINIMALITY.name,
                self.key_list + ["level", "cut_type", "timestamp"],
            ]
            .groupby(self.key_list + ["level", "cut_type"])
            .count()
            .rename(columns={"timestamp": "count_cuts"})
            .reset_index()
        )

    @property
    def avg_cuts(self):
        return (
            self.cut_log.loc[
                self.cut_log["cut_type"] != EnumCutType.MINIMALITY.name,
                self.key_list + ["level", "cut_type", "cut_strength"],
            ]
            .groupby(self.key_list + ["cut_type"])
            # .agg(["mean", "count"])
            .mean()
            .rename(columns={"cut_strength": "num_literals"})
            .reset_index()
        )

    @property
    def count_attractor_size(self):
        count_df = (
            self.solve_log.loc[
                self.solve_log["step"] == EnumBendersStep.LOWER_LEVEL_PROBLEM.name,
                self.key_list + ["model", "timestamp"],
            ]
            .groupby(self.key_list + ["model"])
            .count()
        )
        merged_df = (
            count_df.reset_index()
            .set_index(self.key_list)
            .merge(
                self.solution_count.groupby(self.key_list)
                .sum()
                .reset_index()
                .set_index(self.key_list),
                left_index=True,
                right_index=True,
            )
        )
        merged_df["timestamp"] = merged_df["timestamp"] - merged_df["cut_strength"]
        merged_df.drop(["cut_strength"], axis=1, inplace=True)
        merged_df.rename(columns={"timestamp": "attractors"}, inplace=True)

        return merged_df[merged_df["timestamp"] > 0]

    @property
    def separation_success(self):
        return (
            self.solve_log.loc[
                self.solve_log["step"] == EnumBendersStep.SEPARATION_PROBLEM.name,
                self.key_list + ["step", "feasible", "solve_time"],
            ]
            .groupby(self.key_list + ["step", "feasible"])
            .count()
            .reset_index()
            .rename(columns={"solve_time": "success"})
        )

    @property
    def max_level(self):
        return (
            self.solve_log.loc[
                self.solve_log["step"] == EnumBendersStep.FINISHED.name,
                self.key_list + ["level"],
            ]
            .groupby(self.key_list)
            .max()
            .rename(columns={"level": "max_level"})
            .reset_index()
        )


class Experiment:
    def __init__(
        self, work_dir: str, alg: str, option_names: List[str], options: List[Any]
    ) -> None:
        self.work_dir = work_dir
        self.alg = alg
        self.option_names = option_names
        self.options = options
        self.log_list = [
            BendersAnalysis(
                f"{self.exp_path}\\{inst}\\log__build.txt",
                f"{self.exp_path}\\{inst}\\log__solve.txt",
                f"{self.exp_path}\\{inst}\\log__cut.txt",
                option_names,
                options,
                inst,
            )
            for inst, bn in iter_bn_in_repo()
        ]

    @property
    def exp_path(self):
        return f"{self.work_dir}\\{self.alg}"

    def get_agg_table(self, attr_name: str) -> pd.DataFrame:
        """
        solution_count,
        completion_time,
        build_time,
        count_cuts,
        avg_cuts,
        computation_time,
        separation_success,
        count_attractor_size,
        max_level
        """

        return pd.concat(
            (getattr(log_analysis, attr_name) for log_analysis in self.log_list), axis=0
        )


if __name__ == "__main__":
    import os

    alg = "benders"
    work_dir, options = (
        os.path.dirname(__file__) + "\\230910_allow_empty_attractor_BEN_3",
        ("BEN", True, 3),
    )
    option_names = ["alg", "empty", "T_max"]

    # work_dir = os.path.dirname(__file__) + "\\230909_empty_allow_attractor"

    for inst in ["L4"]:
        log_analysis = BendersAnalysis(
            f"{work_dir}\\{alg}\\{inst}\\log__build.txt",
            f"{work_dir}\\{alg}\\{inst}\\log__solve.txt",
            f"{work_dir}\\{alg}\\{inst}\\log__cut.txt",
            option_names,
            options,
            inst,
        )
        # print(log_analysis.solution_count)
        # print(log_analysis.completion_time)
        # print(log_analysis.build_time)
        # print(log_analysis.count_cuts)
        # print(log_analysis.computation_time)
        # print(log_analysis.separation_success)
        # print(log_analysis.count_attractor_size)
        # log_analysis.count_attractor_size
        # .to_csv(
        #     "attractor_count.csv", header=True
        # )
