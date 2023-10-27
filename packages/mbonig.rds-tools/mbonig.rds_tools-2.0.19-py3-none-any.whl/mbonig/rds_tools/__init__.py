'''
# RDS Tools

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Developer Preview](https://img.shields.io/badge/cdk--constructs-developer--preview-informational.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are in **developer preview** before they
> become stable. We will only make breaking changes to address unforeseen API issues. Therefore,
> these APIs are not subject to [Semantic Versioning](https://semver.org/), and breaking changes
> will be announced in release notes. This means that while you may use them, you may need to
> update your source code when upgrading to a newer version of this package.

---


There are multiple versions of this library published. You should be using the v0.X.X versions for now.
There are versions published that match the CDK version they depend on, but don't use those.

<!--END STABILITY BANNER-->

This is a collection of CDK constructs you can use with RDS.

![Developer Preview](https://img.shields.io/badge/developer--preview-informational.svg?style=for-the-badge)

# DatabaseScript

Provides a Custom Resource and backing Lambda Function that will run a given script against a given database.

```python
const databaseInstance = new DatabaseInstance(stack, 'test-database', {
  engine: DatabaseInstanceEngine.sqlServerWeb({ version: SqlServerEngineVersion.VER_15_00_4043_16_V1 }),
  vpc: vpc,
});


// ...


new DatabaseScript(stack2, 'test', {
  databaseInstance,
  script: 'SELECT 1',
})
  .bind(databaseInstance.connections.securityGroups[0]); // bind for security access
```

# DatabaseUser

There was once a construct called DatabaseUser. However, it is better to use the standard code from the CDK directly:

```python
const myUserSecret = new rds.DatabaseSecret(this, 'MyUserSecret', {
  username: 'myuser',
  masterSecret: instance.secret,
  excludeCharacters: '{}[]()\'"/\\', // defaults to the set " %+~`#$&*()|[]{}:;<>?!'/@\"\\"
});
const myUserSecretAttached = myUserSecret.attach(instance); // Adds DB connections information in the secret
instance.addRotationMultiUser('MyUser', { // Add rotation using the multi user scheme
  secret: myUserSecretAttached,
});
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk.aws_ec2 as _aws_cdk_aws_ec2_ceddda9d
import aws_cdk.aws_lambda as _aws_cdk_aws_lambda_ceddda9d
import aws_cdk.aws_rds as _aws_cdk_aws_rds_ceddda9d
import aws_cdk.aws_secretsmanager as _aws_cdk_aws_secretsmanager_ceddda9d
import constructs as _constructs_77d1e7e8


@jsii.implements(_aws_cdk_aws_ec2_ceddda9d.IConnectable)
class DatabaseScript(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@matthewbonig/rds-tools.DatabaseScript",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        script: builtins.str,
        database_instance: typing.Optional[_aws_cdk_aws_rds_ceddda9d.DatabaseInstance] = None,
        database_name: typing.Optional[builtins.str] = None,
        enable_adhoc: typing.Optional[builtins.bool] = None,
        secret: typing.Optional[_aws_cdk_aws_secretsmanager_ceddda9d.ISecret] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param script: The script to execute.
        :param database_instance: The database instance to run the script against.
        :param database_name: An optional databaseName. If none is provided then it will be the default for the rds instance, as defined by the AWS docs. mysql - mysql mssql - master postgres - postgres
        :param enable_adhoc: Deploy a second Lambda function that allows for adhoc sql against the database? Default: false
        :param secret: An optional secret that provides credentials for the database. Must have fields 'username' and 'password' Default: the root secret from the database instance
        :param vpc: The VPC for the Lambda Function to attach to. If one is not provide, it's assumed from the database instance.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c48c67a79e5f4a984478bfad572dd6d1a7c2f330daa0b4df30943cdddffe8c00)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DatabaseScriptProps(
            script=script,
            database_instance=database_instance,
            database_name=database_name,
            enable_adhoc=enable_adhoc,
            secret=secret,
            vpc=vpc,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        security_group: _aws_cdk_aws_ec2_ceddda9d.SecurityGroup,
        port: _aws_cdk_aws_ec2_ceddda9d.Port,
    ) -> "DatabaseScript":
        '''(deprecated) Grants access to the Lambda Function to the given SecurityGroup.

        Adds an ingress rule to the given security group and for the given port.

        :param security_group: -
        :param port: -

        :deprecated: Do not use, pass this construct as an IConnectable

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1b7ecda0b2ceedc274fa706aec879ef7415eac3a752673d0cccdddb5f52288c)
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        return typing.cast("DatabaseScript", jsii.invoke(self, "bind", [security_group, port]))

    @jsii.member(jsii_name="slugify")
    def slugify(self, x: builtins.str) -> builtins.str:
        '''
        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c502893e2d28537cca0af431386d1fd9c4f7adab6595b2d95c9445425b135532)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.str, jsii.invoke(self, "slugify", [x]))

    @builtins.property
    @jsii.member(jsii_name="adhocConnections")
    def adhoc_connections(self) -> _aws_cdk_aws_ec2_ceddda9d.Connections:
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.Connections, jsii.get(self, "adhocConnections"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> _aws_cdk_aws_ec2_ceddda9d.Connections:
        '''The network connections associated with this resource.'''
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="handler")
    def handler(self) -> _aws_cdk_aws_lambda_ceddda9d.IFunction:
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.IFunction, jsii.get(self, "handler"))

    @builtins.property
    @jsii.member(jsii_name="adhocHandler")
    def adhoc_handler(self) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IFunction]:
        '''The underlying Lambda handler function for making adhoc commands against the database.

        Undefined unless 'enableAdhoc' is true
        '''
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IFunction], jsii.get(self, "adhocHandler"))

    @adhoc_handler.setter
    def adhoc_handler(
        self,
        value: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IFunction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ce633a5b231f50615ccb43ef348945555b9910d89d297fcff79f12093771dfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adhocHandler", value)


@jsii.data_type(
    jsii_type="@matthewbonig/rds-tools.DatabaseScriptProps",
    jsii_struct_bases=[],
    name_mapping={
        "script": "script",
        "database_instance": "databaseInstance",
        "database_name": "databaseName",
        "enable_adhoc": "enableAdhoc",
        "secret": "secret",
        "vpc": "vpc",
    },
)
class DatabaseScriptProps:
    def __init__(
        self,
        *,
        script: builtins.str,
        database_instance: typing.Optional[_aws_cdk_aws_rds_ceddda9d.DatabaseInstance] = None,
        database_name: typing.Optional[builtins.str] = None,
        enable_adhoc: typing.Optional[builtins.bool] = None,
        secret: typing.Optional[_aws_cdk_aws_secretsmanager_ceddda9d.ISecret] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    ) -> None:
        '''
        :param script: The script to execute.
        :param database_instance: The database instance to run the script against.
        :param database_name: An optional databaseName. If none is provided then it will be the default for the rds instance, as defined by the AWS docs. mysql - mysql mssql - master postgres - postgres
        :param enable_adhoc: Deploy a second Lambda function that allows for adhoc sql against the database? Default: false
        :param secret: An optional secret that provides credentials for the database. Must have fields 'username' and 'password' Default: the root secret from the database instance
        :param vpc: The VPC for the Lambda Function to attach to. If one is not provide, it's assumed from the database instance.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4d726a51e54ff23a20242cc842565af0a798f4d6fc59a8ad04ae7d6109ac3ca)
            check_type(argname="argument script", value=script, expected_type=type_hints["script"])
            check_type(argname="argument database_instance", value=database_instance, expected_type=type_hints["database_instance"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument enable_adhoc", value=enable_adhoc, expected_type=type_hints["enable_adhoc"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "script": script,
        }
        if database_instance is not None:
            self._values["database_instance"] = database_instance
        if database_name is not None:
            self._values["database_name"] = database_name
        if enable_adhoc is not None:
            self._values["enable_adhoc"] = enable_adhoc
        if secret is not None:
            self._values["secret"] = secret
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def script(self) -> builtins.str:
        '''The script to execute.'''
        result = self._values.get("script")
        assert result is not None, "Required property 'script' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_instance(
        self,
    ) -> typing.Optional[_aws_cdk_aws_rds_ceddda9d.DatabaseInstance]:
        '''The database instance to run the script against.'''
        result = self._values.get("database_instance")
        return typing.cast(typing.Optional[_aws_cdk_aws_rds_ceddda9d.DatabaseInstance], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''An optional databaseName.

        If none is provided then it will be the default for the rds instance, as defined by the AWS docs.

        mysql - mysql
        mssql - master
        postgres - postgres
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_adhoc(self) -> typing.Optional[builtins.bool]:
        '''Deploy a second Lambda function that allows for adhoc sql against the database?

        :default: false
        '''
        result = self._values.get("enable_adhoc")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def secret(self) -> typing.Optional[_aws_cdk_aws_secretsmanager_ceddda9d.ISecret]:
        '''An optional secret that provides credentials for the database.

        Must have fields 'username' and 'password'

        :default: the root secret from the database instance
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[_aws_cdk_aws_secretsmanager_ceddda9d.ISecret], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc]:
        '''The VPC for the Lambda Function to attach to.

        If one is not provide, it's assumed from the database instance.
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseScriptProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DatabaseScript",
    "DatabaseScriptProps",
]

publication.publish()

def _typecheckingstub__c48c67a79e5f4a984478bfad572dd6d1a7c2f330daa0b4df30943cdddffe8c00(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    script: builtins.str,
    database_instance: typing.Optional[_aws_cdk_aws_rds_ceddda9d.DatabaseInstance] = None,
    database_name: typing.Optional[builtins.str] = None,
    enable_adhoc: typing.Optional[builtins.bool] = None,
    secret: typing.Optional[_aws_cdk_aws_secretsmanager_ceddda9d.ISecret] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1b7ecda0b2ceedc274fa706aec879ef7415eac3a752673d0cccdddb5f52288c(
    security_group: _aws_cdk_aws_ec2_ceddda9d.SecurityGroup,
    port: _aws_cdk_aws_ec2_ceddda9d.Port,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c502893e2d28537cca0af431386d1fd9c4f7adab6595b2d95c9445425b135532(
    x: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ce633a5b231f50615ccb43ef348945555b9910d89d297fcff79f12093771dfd(
    value: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IFunction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4d726a51e54ff23a20242cc842565af0a798f4d6fc59a8ad04ae7d6109ac3ca(
    *,
    script: builtins.str,
    database_instance: typing.Optional[_aws_cdk_aws_rds_ceddda9d.DatabaseInstance] = None,
    database_name: typing.Optional[builtins.str] = None,
    enable_adhoc: typing.Optional[builtins.bool] = None,
    secret: typing.Optional[_aws_cdk_aws_secretsmanager_ceddda9d.ISecret] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
) -> None:
    """Type checking stubs"""
    pass
