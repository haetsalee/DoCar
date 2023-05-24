# generated from rosidl_generator_py/resource/_idl.py.em
# with input from waypoint_navigation_interfaces:srv/AddWp.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AddWp_Request(type):
    """Metaclass of message 'AddWp_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('waypoint_navigation_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'waypoint_navigation_interfaces.srv.AddWp_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__add_wp__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__add_wp__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__add_wp__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__add_wp__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__add_wp__request

            from waypoint_navigation_interfaces.msg import Wp
            if Wp.__class__._TYPE_SUPPORT is None:
                Wp.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AddWp_Request(metaclass=Metaclass_AddWp_Request):
    """Message class 'AddWp_Request'."""

    __slots__ = [
        '_wp',
    ]

    _fields_and_field_types = {
        'wp': 'waypoint_navigation_interfaces/Wp',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['waypoint_navigation_interfaces', 'msg'], 'Wp'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from waypoint_navigation_interfaces.msg import Wp
        self.wp = kwargs.get('wp', Wp())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.wp != other.wp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def wp(self):
        """Message field 'wp'."""
        return self._wp

    @wp.setter
    def wp(self, value):
        if __debug__:
            from waypoint_navigation_interfaces.msg import Wp
            assert \
                isinstance(value, Wp), \
                "The 'wp' field must be a sub message of type 'Wp'"
        self._wp = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_AddWp_Response(type):
    """Metaclass of message 'AddWp_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('waypoint_navigation_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'waypoint_navigation_interfaces.srv.AddWp_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__add_wp__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__add_wp__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__add_wp__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__add_wp__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__add_wp__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AddWp_Response(metaclass=Metaclass_AddWp_Response):
    """Message class 'AddWp_Response'."""

    __slots__ = [
        '_overwrite',
    ]

    _fields_and_field_types = {
        'overwrite': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.overwrite = kwargs.get('overwrite', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.overwrite != other.overwrite:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def overwrite(self):
        """Message field 'overwrite'."""
        return self._overwrite

    @overwrite.setter
    def overwrite(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'overwrite' field must be of type 'bool'"
        self._overwrite = value


class Metaclass_AddWp(type):
    """Metaclass of service 'AddWp'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('waypoint_navigation_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'waypoint_navigation_interfaces.srv.AddWp')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__add_wp

            from waypoint_navigation_interfaces.srv import _add_wp
            if _add_wp.Metaclass_AddWp_Request._TYPE_SUPPORT is None:
                _add_wp.Metaclass_AddWp_Request.__import_type_support__()
            if _add_wp.Metaclass_AddWp_Response._TYPE_SUPPORT is None:
                _add_wp.Metaclass_AddWp_Response.__import_type_support__()


class AddWp(metaclass=Metaclass_AddWp):
    from waypoint_navigation_interfaces.srv._add_wp import AddWp_Request as Request
    from waypoint_navigation_interfaces.srv._add_wp import AddWp_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')