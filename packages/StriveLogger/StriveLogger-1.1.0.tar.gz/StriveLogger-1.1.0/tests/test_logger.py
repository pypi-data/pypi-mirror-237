from assertpy import assert_that

from strivelogger.logger_implementations.console_logger import ConsoleLogger
from strivelogger.logger_implementations.null_logger import NullLogger
from strivelogger.strive_logger import StriveLogger

DEFAULT_LOGGER_NAME = type(NullLogger()).__name__


def test_uses_null_logger_by_default():
    assert_that(StriveLogger.logger_type()).is_equal_to(DEFAULT_LOGGER_NAME)


def test_can_log_debug_message_when_uninitialized():
    StriveLogger.debug("test")


def test_can_log_info_message_when_uninitialized():
    StriveLogger.info("test")


def test_can_log_warn_message_when_uninitialized():
    StriveLogger.warn("test")


def test_can_log_error_message_when_uninitialized():
    StriveLogger.error("test")


def test_cannot_unset_logger():
    StriveLogger.initialize(None)
    assert_that(StriveLogger.logger_type()).is_equal_to(DEFAULT_LOGGER_NAME)


def test_cannot_set_invalid_logger():
    class NotALoggingImplementation:
        pass

    StriveLogger.initialize(NotALoggingImplementation())
    assert_that(StriveLogger.logger_type()).is_equal_to(DEFAULT_LOGGER_NAME)


def test_can_set_valid_logger():
    StriveLogger.initialize(ConsoleLogger())
    assert_that(StriveLogger.logger_type()).is_equal_to(type(ConsoleLogger()).__name__)
