# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [UNRELEASED]

## [0.12.6] - 2023-10-25
### Added
- declare support for type checking
- add support for django 4.2
- add support for python 3.12

### Fixed
- Avoid calling `AutoSchema.get_request_serializer` when inspecting a get operation for possible error responses.

## [0.12.5] - 2023-01-14
### Added
- allow adding extra validation errors on an operation-basis using the new `@extend_validation_errors` decorator.
You can find [more information about that in the documentation](openapi.md#customize-error-codes-on-an-operation-basis).

### Fixed
- use `model._default_manager` instead of `model.objects`.
- Don't generate error responses for OpenAPI callbacks.
- Make `_should_add_http403_error_response` check if permission is `IsAuthenticated` and 
`AllowAny` via `type` instead of `isinstance`
- Don't collect error codes from nested `read_only` fields

## [0.12.4] - 2022-12-11
### Fixed
- account for specifying the request serializer as a basic type (like `OpenApiTypes.STR`) or as a
`PolymorphicProxySerializer` using `@extend_schema(request=...)` when determining error codes for validation errors.

## [0.12.3] - 2022-11-13
### Added
- add support for python 3.11

## [0.12.2] - 2022-09-25
### Added
- When a custom validator class defines a `code` attribute, add it to the list of error codes of raised by
the corresponding field.
- add support for DRF 3.14

## [0.12.1] - 2022-09-03
### Fixed
- generate the mapping for discriminator fields properly instead of showing a "null" value in the generated schema (#12).

## [0.12.0] - 2022-08-27
### Added
- add support for automatically generating error responses schema with [drf-spectacular](https://github.com/tfranzel/drf-spectacular).
Check out the [corresponding documentation page](https://drf-standardized-errors.readthedocs.io/en/latest/openapi.html)
to know more about the integration with drf-spectacular.
- add support for django 4.1

## [0.11.0] - 2022-06-24
### Changed (Backward-incompatible)
- Removed all imports from `drf_standardized_errors.__init__.py`. This avoids facing the `AppRegistryNotReady` error
in certain situations (fixes #7). This change **only affects where functions/classes are imported from**, there are
**no changes to how they work**. To upgrade to this version, you need to:
  - Update the `"EXCEPTION_HANDLER"` setting in `REST_FRAMEWORK` to `"drf_standardized_errors.handler.exception_handler"`.
  - If you imported the exception handler directly, make sure the import looks like this
  `from drf_standardized_errors.handler import exception_handler`.
  - If you imported the exception handler class, make sure the import looks like this
  `from drf_standardized_errors.handler import ExceptionHandler`.
  - If you imported the exception formatter class, make sure the import looks like this
  `from drf_standardized_errors.formatter import ExceptionFormatter`.

## [0.10.2] - 2022-05-08
### Fixed
- disable tag creation by the "create GitHub release" action since it is already created by tbump

## [0.10.1] - 2022-05-08
### Fixed
- add write permission to create release action, so it can push release notes to GitHub
- fix license badge link so it works on PyPI

## [0.10.0] - 2022-05-08
### Added

- Build the documentation automatically on every commit to the main branch. The docs are
[hosted on readthedocs](https://drf-standardized-errors.readthedocs.io/en/latest/).
- Add package metadata
- add a GitHub workflow to create a GitHub release when a new tag is pushed
- add a GitHub workflow to run tests on every push and pull request
- add test coverage

## [0.9.0] - 2022-05-07
### Added

- Common error response format for DRF-based APIs
- Easily customize the error response format.
- Handle error responses for list serializers and nested serializers. 
- Add documentation
- Add tests
- Automate release steps
