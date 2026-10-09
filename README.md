# Лаба 1 из 2 семестра

Тестирование:

```zsh
% pytest -v

============================================================================ test session starts =============================================================================
platform darwin -- Python 3.9.6, pytest-7.4.3, pluggy-1.6.0 -- /Users/ksenia/Documents/itmo/академ разница/прога/lab2-sem-1/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/ksenia/Documents/itmo/академ разница/прога/lab2-sem-1
collected 22 items                                                                                                                                                           

task1_logger/test_logger.py::TestLoggerDecorator::test_logs_exception PASSED                                                                                           [  4%]
task1_logger/test_logger.py::TestLoggerDecorator::test_logs_function_name_args_and_result PASSED                                                                       [  9%]
task1_logger/test_logger.py::TestLoggerDecorator::test_logs_kwargs PASSED                                                                                              [ 13%]
task1_logger/test_logger.py::TestLoggerDecorator::test_preserves_metadata PASSED                                                                                       [ 18%]
task2_retry/test_retry.py::TestRetryDecorator::test_all_attempts_fail PASSED                                                                                           [ 22%]
task2_retry/test_retry.py::TestRetryDecorator::test_delay_between_attempts PASSED                                                                                      [ 27%]
task2_retry/test_retry.py::TestRetryDecorator::test_exception_filter_passes_through PASSED                                                                             [ 31%]
task2_retry/test_retry.py::TestRetryDecorator::test_invalid_arguments PASSED                                                                                           [ 36%]
task2_retry/test_retry.py::TestRetryDecorator::test_no_retry_when_success PASSED                                                                                       [ 40%]
task2_retry/test_retry.py::TestRetryDecorator::test_retry_until_success PASSED                                                                                         [ 45%]
task3_class_logger/test_class_logger.py::TestClassLogger::test_magic_methods_disabled PASSED                                                                           [ 50%]
task3_class_logger/test_class_logger.py::TestClassLogger::test_magic_methods_logged_by_default PASSED                                                                  [ 54%]
task3_class_logger/test_class_logger.py::TestClassLogger::test_regular_methods_logged PASSED                                                                           [ 59%]
task3_class_logger/test_class_logger.py::TestClassLogger::test_static_and_class_methods PASSED                                                                         [ 63%]
task4_call_limiter/test_call_limiter.py::TestCallLimiter::test_allows_up_to_limit PASSED                                                                               [ 68%]
task4_call_limiter/test_call_limiter.py::TestCallLimiter::test_counters_are_independent_per_method PASSED                                                              [ 72%]
task4_call_limiter/test_call_limiter.py::TestCallLimiter::test_exceeding_limit_raises PASSED                                                                           [ 77%]
task4_call_limiter/test_call_limiter.py::TestCallLimiter::test_invalid_limit PASSED                                                                                    [ 81%]
task4_call_limiter/test_call_limiter.py::TestCallLimiter::test_static_and_class_methods PASSED                                                                         [ 86%]
task5_async/test_async_demo.py::TestAsyncDemo::test_runs_concurrently PASSED                                                                                           [ 90%]
task5_async/test_async_demo.py::TestAsyncDemo::test_task_first_prints_three_lines PASSED                                                                               [ 95%]
task5_async/test_async_demo.py::TestAsyncDemo::test_task_second_prints_four_lines PASSED                                                                               [100%]

============================================================================= 22 passed in 0.47s =============================================================================
```
