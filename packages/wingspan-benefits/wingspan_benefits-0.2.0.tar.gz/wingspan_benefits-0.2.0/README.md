# openapi

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/wingspanHQ/client-sdk-python.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/wingspanHQ/client-sdk-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README
<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install wingspan_benefits
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations

s = sdk.SDK()


res = s.sdk.get_benefits_enrollment_id_(id='string')

if res.enrollment is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations

### [SDK](docs/sdks/sdk/README.md)

* [get_benefits_enrollment_id_](docs/sdks/sdk/README.md#get_benefits_enrollment_id_) - Retrieve Enrollment Details for a Specific Member
* [get_benefits_plan_enrollment](docs/sdks/sdk/README.md#get_benefits_plan_enrollment) - List all plan enrollments
* [get_benefits_plan_enrollment_id_](docs/sdks/sdk/README.md#get_benefits_plan_enrollment_id_) - Get a particular plan enrollment by ID
* [get_benefits_service](docs/sdks/sdk/README.md#get_benefits_service) - Retrieve Current Benefits Service Status
* [patch_benefits_service_id_](docs/sdks/sdk/README.md#patch_benefits_service_id_) - Modify Benefits Service Status
<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->

<!-- End Dev Containers -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
