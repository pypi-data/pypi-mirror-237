class IdentityProvisioningFailed(Exception):
    pass


class StopEnvironmentFailed(Exception):
    pass


class StartEnvironmentFailed(Exception):
    pass


class DeleteEnvironmentFailed(Exception):
    pass


class ChangeEnvironmentInstanceTypeFailed(Exception):
    pass


class EnvironmentCreationFailed(Exception):
    pass


class BillingVerificationFailed(Exception):
    pass


class BillingSharingFailed(Exception):
    pass


class BillingAccessRevokationFailed(Exception):
    pass


class GetAvailableEnvironmentsFailed(Exception):
    pass


class GetUserInfoFailed(Exception):
    pass


class GetWorkspaceDetailsFailed(Exception):
    pass


class GetBillingAccountsListFailed(Exception):
    pass


class GetWorkspacesListFailed(Exception):
    pass


class CreateWorkspaceFailed(Exception):
    pass


class DeleteWorkspaceFailed(Exception):
    pass


class GetWorkflowFailed(Exception):
    pass
