"""Test factories for generating test data."""

import factory
from django.contrib.auth import get_user_model
from faker import Faker

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    """Factory for generating test users."""

    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')

class SwitchFactory(factory.django.DjangoModelFactory):
    """Factory for generating test switches."""

    class Meta:
        model = 'switches.Switch'

    name = factory.Sequence(lambda n: f'switch{n}')
    ip_address = factory.LazyFunction(lambda: fake.ipv4())
    username = factory.LazyFunction(lambda: fake.user_name())
    password = factory.LazyFunction(lambda: fake.password())
    description = factory.LazyFunction(lambda: fake.sentence())

class PortFactory(factory.django.DjangoModelFactory):
    """Factory for generating test ports."""

    class Meta:
        model = 'switches.Port'

    switch = factory.SubFactory(SwitchFactory)
    name = factory.Sequence(lambda n: f'1/0/{n}')
    description = factory.LazyFunction(lambda: fake.sentence())
    admin_status = factory.Iterator(['up', 'down'])
    vlan = factory.LazyFunction(lambda: fake.random_int(min=1, max=4094))
    speed = factory.Iterator(['auto', '1G', '10G', '40G'])
    duplex = factory.Iterator(['full', 'half', 'auto'])

class ConfigurationFactory(factory.django.DjangoModelFactory):
    """Factory for generating test configurations."""

    class Meta:
        model = 'switches.Configuration'

    switch = factory.SubFactory(SwitchFactory)
    content = factory.LazyFunction(lambda: fake.text())
    version = factory.Sequence(lambda n: f'1.{n}')
    description = factory.LazyFunction(lambda: fake.sentence())
