from backbone.entities import Entity


def test_entity_composition():
    class TestObject:
        def __init__(self, value):
            self.value = value

    class TestComponent:
        def __init__(self, component_value):
            self.component_value = component_value

    entity = Entity(TestObject("object"))
    entity.add_component(TestComponent("component"))
    obj = entity.get_flattened_object(TestComponent)
    assert obj.value == "object"
    assert obj.component_value == "component"


def test_entity_multiple_composition():
    class TestObject:
        def __init__(self, value):
            self.value = value

    class TestComponentA:
        def __init__(self, component_value):
            self.a = component_value

    class TestComponentB:
        def __init__(self, component_value):
            self.b = component_value

    entity = Entity(TestObject("object"))
    entity.add_component(TestComponentA("component A"))
    entity.add_component(TestComponentB("component B"))
    obj = entity.get_flattened_object(TestComponentA, TestComponentB)
    assert obj.value == "object"
    assert obj.a == "component A"
    assert obj.b == "component B"
