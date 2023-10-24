import logging


class InvalidConfigError(Exception):
    pass


class InvalidConfigWarning(Warning):
    pass


class EmptySolutionError(Exception):
    pass


class EmptyAttractorError(Warning):
    pass


# class SuppressAllWarning(object):
#     """Suppress all warning message from solve()."""

#     class AllWarningFilter(logging.Filter):
#         def filter(self, record):
#             return True

#     warning_filter = AllWarningFilter()

#     def __enter__(self):
#         logger = logging.getLogger("pyomo.core")
#         logger.addFilter(self.warning_filter)
#         return self

#     def __exit__(self, exception_type, exception_value, traceback):
#         logger = logging.getLogger("pyomo.core")
#         logger.removeFilter(self.warning_filter)
