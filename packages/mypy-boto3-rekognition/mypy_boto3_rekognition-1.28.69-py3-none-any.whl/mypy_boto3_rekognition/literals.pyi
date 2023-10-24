"""
Type annotations for rekognition service literal definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/literals/)

Usage::

    ```python
    from mypy_boto3_rekognition.literals import AttributeType

    data: AttributeType = "AGE_RANGE"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AttributeType",
    "BodyPartType",
    "CelebrityRecognitionSortByType",
    "ContentClassifierType",
    "ContentModerationAggregateByType",
    "ContentModerationSortByType",
    "CustomizationFeatureType",
    "DatasetStatusMessageCodeType",
    "DatasetStatusType",
    "DatasetTypeType",
    "DescribeProjectVersionsPaginatorName",
    "DescribeProjectsPaginatorName",
    "DetectLabelsFeatureNameType",
    "EmotionNameType",
    "FaceAttributesType",
    "FaceSearchSortByType",
    "GenderTypeType",
    "KnownGenderTypeType",
    "LabelDetectionAggregateByType",
    "LabelDetectionFeatureNameType",
    "LabelDetectionSortByType",
    "LandmarkTypeType",
    "ListCollectionsPaginatorName",
    "ListDatasetEntriesPaginatorName",
    "ListDatasetLabelsPaginatorName",
    "ListFacesPaginatorName",
    "ListProjectPoliciesPaginatorName",
    "ListStreamProcessorsPaginatorName",
    "ListUsersPaginatorName",
    "LivenessSessionStatusType",
    "MediaAnalysisJobFailureCodeType",
    "MediaAnalysisJobStatusType",
    "OrientationCorrectionType",
    "PersonTrackingSortByType",
    "ProjectAutoUpdateType",
    "ProjectStatusType",
    "ProjectVersionRunningWaiterName",
    "ProjectVersionStatusType",
    "ProjectVersionTrainingCompletedWaiterName",
    "ProtectiveEquipmentTypeType",
    "QualityFilterType",
    "ReasonType",
    "SegmentTypeType",
    "StreamProcessorParameterToDeleteType",
    "StreamProcessorStatusType",
    "TechnicalCueTypeType",
    "TextTypesType",
    "UnsearchedFaceReasonType",
    "UnsuccessfulFaceAssociationReasonType",
    "UnsuccessfulFaceDeletionReasonType",
    "UnsuccessfulFaceDisassociationReasonType",
    "UserStatusType",
    "VideoColorRangeType",
    "VideoJobStatusType",
    "RekognitionServiceName",
    "ServiceName",
    "ResourceServiceName",
    "PaginatorName",
    "WaiterName",
    "RegionName",
)

AttributeType = Literal[
    "AGE_RANGE",
    "ALL",
    "BEARD",
    "DEFAULT",
    "EMOTIONS",
    "EYEGLASSES",
    "EYES_OPEN",
    "EYE_DIRECTION",
    "FACE_OCCLUDED",
    "GENDER",
    "MOUTH_OPEN",
    "MUSTACHE",
    "SMILE",
    "SUNGLASSES",
]
BodyPartType = Literal["FACE", "HEAD", "LEFT_HAND", "RIGHT_HAND"]
CelebrityRecognitionSortByType = Literal["ID", "TIMESTAMP"]
ContentClassifierType = Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
ContentModerationAggregateByType = Literal["SEGMENTS", "TIMESTAMPS"]
ContentModerationSortByType = Literal["NAME", "TIMESTAMP"]
CustomizationFeatureType = Literal["CONTENT_MODERATION", "CUSTOM_LABELS"]
DatasetStatusMessageCodeType = Literal["CLIENT_ERROR", "SERVICE_ERROR", "SUCCESS"]
DatasetStatusType = Literal[
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
DatasetTypeType = Literal["TEST", "TRAIN"]
DescribeProjectVersionsPaginatorName = Literal["describe_project_versions"]
DescribeProjectsPaginatorName = Literal["describe_projects"]
DetectLabelsFeatureNameType = Literal["GENERAL_LABELS", "IMAGE_PROPERTIES"]
EmotionNameType = Literal[
    "ANGRY", "CALM", "CONFUSED", "DISGUSTED", "FEAR", "HAPPY", "SAD", "SURPRISED", "UNKNOWN"
]
FaceAttributesType = Literal["ALL", "DEFAULT"]
FaceSearchSortByType = Literal["INDEX", "TIMESTAMP"]
GenderTypeType = Literal["Female", "Male"]
KnownGenderTypeType = Literal["Female", "Male", "Nonbinary", "Unlisted"]
LabelDetectionAggregateByType = Literal["SEGMENTS", "TIMESTAMPS"]
LabelDetectionFeatureNameType = Literal["GENERAL_LABELS"]
LabelDetectionSortByType = Literal["NAME", "TIMESTAMP"]
LandmarkTypeType = Literal[
    "chinBottom",
    "eyeLeft",
    "eyeRight",
    "leftEyeBrowLeft",
    "leftEyeBrowRight",
    "leftEyeBrowUp",
    "leftEyeDown",
    "leftEyeLeft",
    "leftEyeRight",
    "leftEyeUp",
    "leftPupil",
    "midJawlineLeft",
    "midJawlineRight",
    "mouthDown",
    "mouthLeft",
    "mouthRight",
    "mouthUp",
    "nose",
    "noseLeft",
    "noseRight",
    "rightEyeBrowLeft",
    "rightEyeBrowRight",
    "rightEyeBrowUp",
    "rightEyeDown",
    "rightEyeLeft",
    "rightEyeRight",
    "rightEyeUp",
    "rightPupil",
    "upperJawlineLeft",
    "upperJawlineRight",
]
ListCollectionsPaginatorName = Literal["list_collections"]
ListDatasetEntriesPaginatorName = Literal["list_dataset_entries"]
ListDatasetLabelsPaginatorName = Literal["list_dataset_labels"]
ListFacesPaginatorName = Literal["list_faces"]
ListProjectPoliciesPaginatorName = Literal["list_project_policies"]
ListStreamProcessorsPaginatorName = Literal["list_stream_processors"]
ListUsersPaginatorName = Literal["list_users"]
LivenessSessionStatusType = Literal["CREATED", "EXPIRED", "FAILED", "IN_PROGRESS", "SUCCEEDED"]
MediaAnalysisJobFailureCodeType = Literal[
    "ACCESS_DENIED",
    "INTERNAL_ERROR",
    "INVALID_KMS_KEY",
    "INVALID_MANIFEST",
    "INVALID_OUTPUT_CONFIG",
    "INVALID_S3_OBJECT",
    "RESOURCE_NOT_FOUND",
    "RESOURCE_NOT_READY",
    "THROTTLED",
]
MediaAnalysisJobStatusType = Literal["CREATED", "FAILED", "IN_PROGRESS", "QUEUED", "SUCCEEDED"]
OrientationCorrectionType = Literal["ROTATE_0", "ROTATE_180", "ROTATE_270", "ROTATE_90"]
PersonTrackingSortByType = Literal["INDEX", "TIMESTAMP"]
ProjectAutoUpdateType = Literal["DISABLED", "ENABLED"]
ProjectStatusType = Literal["CREATED", "CREATING", "DELETING"]
ProjectVersionRunningWaiterName = Literal["project_version_running"]
ProjectVersionStatusType = Literal[
    "COPYING_COMPLETED",
    "COPYING_FAILED",
    "COPYING_IN_PROGRESS",
    "DELETING",
    "DEPRECATED",
    "EXPIRED",
    "FAILED",
    "RUNNING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "TRAINING_COMPLETED",
    "TRAINING_FAILED",
    "TRAINING_IN_PROGRESS",
]
ProjectVersionTrainingCompletedWaiterName = Literal["project_version_training_completed"]
ProtectiveEquipmentTypeType = Literal["FACE_COVER", "HAND_COVER", "HEAD_COVER"]
QualityFilterType = Literal["AUTO", "HIGH", "LOW", "MEDIUM", "NONE"]
ReasonType = Literal[
    "EXCEEDS_MAX_FACES",
    "EXTREME_POSE",
    "LOW_BRIGHTNESS",
    "LOW_CONFIDENCE",
    "LOW_FACE_QUALITY",
    "LOW_SHARPNESS",
    "SMALL_BOUNDING_BOX",
]
SegmentTypeType = Literal["SHOT", "TECHNICAL_CUE"]
StreamProcessorParameterToDeleteType = Literal["ConnectedHomeMinConfidence", "RegionsOfInterest"]
StreamProcessorStatusType = Literal[
    "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "UPDATING"
]
TechnicalCueTypeType = Literal[
    "BlackFrames", "ColorBars", "Content", "EndCredits", "OpeningCredits", "Slate", "StudioLogo"
]
TextTypesType = Literal["LINE", "WORD"]
UnsearchedFaceReasonType = Literal[
    "EXCEEDS_MAX_FACES",
    "EXTREME_POSE",
    "FACE_NOT_LARGEST",
    "LOW_BRIGHTNESS",
    "LOW_CONFIDENCE",
    "LOW_FACE_QUALITY",
    "LOW_SHARPNESS",
    "SMALL_BOUNDING_BOX",
]
UnsuccessfulFaceAssociationReasonType = Literal[
    "ASSOCIATED_TO_A_DIFFERENT_USER", "FACE_NOT_FOUND", "LOW_MATCH_CONFIDENCE"
]
UnsuccessfulFaceDeletionReasonType = Literal["ASSOCIATED_TO_AN_EXISTING_USER", "FACE_NOT_FOUND"]
UnsuccessfulFaceDisassociationReasonType = Literal[
    "ASSOCIATED_TO_A_DIFFERENT_USER", "FACE_NOT_FOUND"
]
UserStatusType = Literal["ACTIVE", "CREATED", "CREATING", "UPDATING"]
VideoColorRangeType = Literal["FULL", "LIMITED"]
VideoJobStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
RekognitionServiceName = Literal["rekognition"]
ServiceName = Literal[
    "accessanalyzer",
    "account",
    "acm",
    "acm-pca",
    "alexaforbusiness",
    "amp",
    "amplify",
    "amplifybackend",
    "amplifyuibuilder",
    "apigateway",
    "apigatewaymanagementapi",
    "apigatewayv2",
    "appconfig",
    "appconfigdata",
    "appfabric",
    "appflow",
    "appintegrations",
    "application-autoscaling",
    "application-insights",
    "applicationcostprofiler",
    "appmesh",
    "apprunner",
    "appstream",
    "appsync",
    "arc-zonal-shift",
    "athena",
    "auditmanager",
    "autoscaling",
    "autoscaling-plans",
    "backup",
    "backup-gateway",
    "backupstorage",
    "batch",
    "bedrock",
    "bedrock-runtime",
    "billingconductor",
    "braket",
    "budgets",
    "ce",
    "chime",
    "chime-sdk-identity",
    "chime-sdk-media-pipelines",
    "chime-sdk-meetings",
    "chime-sdk-messaging",
    "chime-sdk-voice",
    "cleanrooms",
    "cloud9",
    "cloudcontrol",
    "clouddirectory",
    "cloudformation",
    "cloudfront",
    "cloudhsm",
    "cloudhsmv2",
    "cloudsearch",
    "cloudsearchdomain",
    "cloudtrail",
    "cloudtrail-data",
    "cloudwatch",
    "codeartifact",
    "codebuild",
    "codecatalyst",
    "codecommit",
    "codedeploy",
    "codeguru-reviewer",
    "codeguru-security",
    "codeguruprofiler",
    "codepipeline",
    "codestar",
    "codestar-connections",
    "codestar-notifications",
    "cognito-identity",
    "cognito-idp",
    "cognito-sync",
    "comprehend",
    "comprehendmedical",
    "compute-optimizer",
    "config",
    "connect",
    "connect-contact-lens",
    "connectcampaigns",
    "connectcases",
    "connectparticipant",
    "controltower",
    "cur",
    "customer-profiles",
    "databrew",
    "dataexchange",
    "datapipeline",
    "datasync",
    "datazone",
    "dax",
    "detective",
    "devicefarm",
    "devops-guru",
    "directconnect",
    "discovery",
    "dlm",
    "dms",
    "docdb",
    "docdb-elastic",
    "drs",
    "ds",
    "dynamodb",
    "dynamodbstreams",
    "ebs",
    "ec2",
    "ec2-instance-connect",
    "ecr",
    "ecr-public",
    "ecs",
    "efs",
    "eks",
    "elastic-inference",
    "elasticache",
    "elasticbeanstalk",
    "elastictranscoder",
    "elb",
    "elbv2",
    "emr",
    "emr-containers",
    "emr-serverless",
    "entityresolution",
    "es",
    "events",
    "evidently",
    "finspace",
    "finspace-data",
    "firehose",
    "fis",
    "fms",
    "forecast",
    "forecastquery",
    "frauddetector",
    "fsx",
    "gamelift",
    "glacier",
    "globalaccelerator",
    "glue",
    "grafana",
    "greengrass",
    "greengrassv2",
    "groundstation",
    "guardduty",
    "health",
    "healthlake",
    "honeycode",
    "iam",
    "identitystore",
    "imagebuilder",
    "importexport",
    "inspector",
    "inspector2",
    "internetmonitor",
    "iot",
    "iot-data",
    "iot-jobs-data",
    "iot-roborunner",
    "iot1click-devices",
    "iot1click-projects",
    "iotanalytics",
    "iotdeviceadvisor",
    "iotevents",
    "iotevents-data",
    "iotfleethub",
    "iotfleetwise",
    "iotsecuretunneling",
    "iotsitewise",
    "iotthingsgraph",
    "iottwinmaker",
    "iotwireless",
    "ivs",
    "ivs-realtime",
    "ivschat",
    "kafka",
    "kafkaconnect",
    "kendra",
    "kendra-ranking",
    "keyspaces",
    "kinesis",
    "kinesis-video-archived-media",
    "kinesis-video-media",
    "kinesis-video-signaling",
    "kinesis-video-webrtc-storage",
    "kinesisanalytics",
    "kinesisanalyticsv2",
    "kinesisvideo",
    "kms",
    "lakeformation",
    "lambda",
    "lex-models",
    "lex-runtime",
    "lexv2-models",
    "lexv2-runtime",
    "license-manager",
    "license-manager-linux-subscriptions",
    "license-manager-user-subscriptions",
    "lightsail",
    "location",
    "logs",
    "lookoutequipment",
    "lookoutmetrics",
    "lookoutvision",
    "m2",
    "machinelearning",
    "macie",
    "macie2",
    "managedblockchain",
    "managedblockchain-query",
    "marketplace-catalog",
    "marketplace-entitlement",
    "marketplacecommerceanalytics",
    "mediaconnect",
    "mediaconvert",
    "medialive",
    "mediapackage",
    "mediapackage-vod",
    "mediapackagev2",
    "mediastore",
    "mediastore-data",
    "mediatailor",
    "medical-imaging",
    "memorydb",
    "meteringmarketplace",
    "mgh",
    "mgn",
    "migration-hub-refactor-spaces",
    "migrationhub-config",
    "migrationhuborchestrator",
    "migrationhubstrategy",
    "mobile",
    "mq",
    "mturk",
    "mwaa",
    "neptune",
    "neptunedata",
    "network-firewall",
    "networkmanager",
    "nimble",
    "oam",
    "omics",
    "opensearch",
    "opensearchserverless",
    "opsworks",
    "opsworkscm",
    "organizations",
    "osis",
    "outposts",
    "panorama",
    "payment-cryptography",
    "payment-cryptography-data",
    "pca-connector-ad",
    "personalize",
    "personalize-events",
    "personalize-runtime",
    "pi",
    "pinpoint",
    "pinpoint-email",
    "pinpoint-sms-voice",
    "pinpoint-sms-voice-v2",
    "pipes",
    "polly",
    "pricing",
    "privatenetworks",
    "proton",
    "qldb",
    "qldb-session",
    "quicksight",
    "ram",
    "rbin",
    "rds",
    "rds-data",
    "redshift",
    "redshift-data",
    "redshift-serverless",
    "rekognition",
    "resiliencehub",
    "resource-explorer-2",
    "resource-groups",
    "resourcegroupstaggingapi",
    "robomaker",
    "rolesanywhere",
    "route53",
    "route53-recovery-cluster",
    "route53-recovery-control-config",
    "route53-recovery-readiness",
    "route53domains",
    "route53resolver",
    "rum",
    "s3",
    "s3control",
    "s3outposts",
    "sagemaker",
    "sagemaker-a2i-runtime",
    "sagemaker-edge",
    "sagemaker-featurestore-runtime",
    "sagemaker-geospatial",
    "sagemaker-metrics",
    "sagemaker-runtime",
    "savingsplans",
    "scheduler",
    "schemas",
    "sdb",
    "secretsmanager",
    "securityhub",
    "securitylake",
    "serverlessrepo",
    "service-quotas",
    "servicecatalog",
    "servicecatalog-appregistry",
    "servicediscovery",
    "ses",
    "sesv2",
    "shield",
    "signer",
    "simspaceweaver",
    "sms",
    "sms-voice",
    "snow-device-management",
    "snowball",
    "sns",
    "sqs",
    "ssm",
    "ssm-contacts",
    "ssm-incidents",
    "ssm-sap",
    "sso",
    "sso-admin",
    "sso-oidc",
    "stepfunctions",
    "storagegateway",
    "sts",
    "support",
    "support-app",
    "swf",
    "synthetics",
    "textract",
    "timestream-query",
    "timestream-write",
    "tnb",
    "transcribe",
    "transfer",
    "translate",
    "verifiedpermissions",
    "voice-id",
    "vpc-lattice",
    "waf",
    "waf-regional",
    "wafv2",
    "wellarchitected",
    "wisdom",
    "workdocs",
    "worklink",
    "workmail",
    "workmailmessageflow",
    "workspaces",
    "workspaces-web",
    "xray",
]
ResourceServiceName = Literal[
    "cloudformation",
    "cloudwatch",
    "dynamodb",
    "ec2",
    "glacier",
    "iam",
    "opsworks",
    "s3",
    "sns",
    "sqs",
]
PaginatorName = Literal[
    "describe_project_versions",
    "describe_projects",
    "list_collections",
    "list_dataset_entries",
    "list_dataset_labels",
    "list_faces",
    "list_project_policies",
    "list_stream_processors",
    "list_users",
]
WaiterName = Literal["project_version_running", "project_version_training_completed"]
RegionName = Literal[
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "il-central-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
