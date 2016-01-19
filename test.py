# Python module imports.
import sys


# Formatting strings for the invalid maths checks.
MATH_CHECK_STRINGS = [
    "%s + 1",
    "1 + %s",
    "%s - 1",
    "1 - %s",
    "%s * 1",
    "1 * %s",
    "%s / 1",
    "1 / %s",
]


def invalid_math_check(node=None, type=None):
    """Test out the invalid mathematical operation.

    @keyword node:  The Python Node object.
    @type node:     prop_tree.Node instance
    @keyword type:  The object type for the node.
    @type type:     str
    """

    # Loop over the 8 different operations.
    for i in range(8):
        try:
            if i == 0:
                node + 1
            elif i == 1:
                1 + node
            elif i == 2:
                node - 1
            elif i == 3:
                1 - node
            elif i == 4:
                node * 1
            elif i == 5:
                1 * node
            elif i == 6:
                node / 1
            elif i == 7:
                1 / node
            raise NameError("TypeError not raised.")
        except TypeError:
            print("Correct TypeError for %s" % MATH_CHECK_STRINGS[i] % type)


def test_bool(title=None, name=None, value_true=None, value_false=None):
    """Test the boolean qualities of the Node object.

    @keyword title:         The check title.
    @type title:            str
    @keyword name:          The name of the property tree Python object.
    @type name:             str
    @keyword value_true:    The property tree node value that should evaluate to True.
    @type value_true:       object
    @keyword value_false:   The property tree node value that should evaluate to False.
    @type value_false:      object
    """

    # Truth checks.
    ###############

    # Set the value.
    setattr(props, name, value_true)

    # Get the node object.
    obj = getattr(props, name)
    sys.stdout.write("Truth check for the %s object %s: Test " % (title, repr(obj)))

    # Bool checks.
    if obj:
        sys.stdout.write("passed.\n")
    else:
        sys.stdout.write("failed.\n")
        raise NameError("Test failure")


    # Falsity checks.
    #################

    # Set the value.
    setattr(props, name, value_false)
    sys.stdout.write("Falsity check for the %s object %s: Test " % (title, repr(obj)))

    # Bool checks.
    if obj:
        sys.stdout.write("failed.\n")
        raise NameError("Test failure")
    else:
        sys.stdout.write("passed.\n")


def test_equality(name=None, value=-1, eq=-1, ne=-1, le=-1, ge=-1, lt=-1, gt=-1):
    """Test the various equality operators on the node object.

    @keyword name:      The name of the property tree Python object.
    @type name:         str
    @keyword value:     The optional value to set the property tree node to (e.g. to create it).
    @type value:        object
    @keyword eq:        The value that should be equal (==) to the node value.
    @type eq:           object
    @keyword ne:        The value that should not be equal (!=) to the node value.
    @type eq:           object
    @keyword le:        The value that should be less than or equal (<=) to the node value.
    @type le:           list of objects
    @keyword ge:        The value that should be greater than or equal (>=) to the node value.
    @type ge:           list of objects
    @keyword lt:        The value that should be less than (<) to the node value.
    @type lt:           object
    @keyword gt:        The value that should be greater than (>) to the node value.
    @type gt:           object
    """

    # Init.
    flag = True

    # Set the value.
    if value != -1:
        setattr(props, name, value)

    # Get the node object.
    obj = getattr(props, name)
    sys.stdout.write("Equality testing of '%s':\n" % obj)

    # Equality (==) test.
    if eq != -1:
        sys.stdout.write("\tTesting if \"props.%s == %s\": Test " % (name, eq))
        result = "failed"
        try:
            if obj == eq:
                result = "passed"
            else:
                flag = False
        except TypeError:
            sys.stdout.write("failed - TypeError.\n")
            flag = False
        else:
            sys.stdout.write("%s.\n" % result)

    # Inequality (!=) test.
    if ne != -1:
        sys.stdout.write("\tTesting if \"props.%s != %s\": Test " % (name, ne))
        result = "failed"
        try:
            if obj != ne:
                result = "passed"
            else:
                flag = False
        except TypeError:
            sys.stdout.write("failed - TypeError.\n")
            flag = False
        else:
            sys.stdout.write("%s.\n" % result)

    # Less than or equal (<=) test.
    if le != -1:
        for le_item in le:
            sys.stdout.write("\tTesting if \"props.%s <= %s\": Test " % (name, le_item))
            result = "failed"
            try:
                if obj <= le_item:
                    result = "passed"
                else:
                    flag = False
            except TypeError:
                sys.stdout.write("failed - TypeError.\n")
                flag = False
            else:
                sys.stdout.write("%s.\n" % result)

    # Greater than or equal (>=) test.
    if ge != -1:
        for ge_item in ge:
            sys.stdout.write("\tTesting if \"props.%s >= %s\": Test " % (name, ge_item))
            result = "failed"
            try:
                if obj >= ge_item:
                    result = "passed"
                else:
                    flag = False
            except TypeError:
                sys.stdout.write("failed - TypeError.\n")
                flag = False
            else:
                sys.stdout.write("%s.\n" % result)

    # Less than (<) test.
    if lt != -1:
        sys.stdout.write("\tTesting if \"props.%s < %s\": Test " % (name, lt))
        result = "failed"
        try:
            if obj < lt:
                result = "passed"
            else:
                flag = False
        except TypeError:
            sys.stdout.write("failed - TypeError.\n")
            flag = False
        else:
            sys.stdout.write("%s.\n" % result)

    # Greater than (>) test.
    if gt != -1:
        sys.stdout.write("\tTesting if \"props.%s > %s\": Test " % (name, gt))
        result = "failed"
        try:
            if obj > gt:
                result = "passed"
            else:
                flag = False
        except TypeError:
            sys.stdout.write("failed - TypeError.\n")
            flag = False
        else:
            sys.stdout.write("%s.\n" % result)

    # Failure of the tests.
    if not flag:
        raise NameError("Test failure.")


def test_length(name=None, length=0):
    """Test the length of the property tree array.

    @keyword name:      The name of the property tree Python object.
    @type name:         str
    @keyword length:    The expected length.
    @type length:       int
    """

    node = getattr(props, name)
    print(repr(node))
    __len__ = len(node)
    print("The props.%s length: %s (should be %s)." % (name, __len__, length))
    if __len__ != length:
        raise NameError("The props.%s length of %i is incorrect." % (name, __len__))


def test_string_repr(name=None, value=-1, repr=None):
    """Test the string representation of a Node object.

    @keyword name:      The name of the property tree Python object.
    @type name:         str
    @keyword value:     The optional value to set the property tree node to (e.g. to create it).
    @type value:        object
    """

    # Set the value.
    if value != -1:
        setattr(props, name, value)

    # The value and string repr are the same.
    if not repr:
        repr = value

    # The string representation of the node object.
    obj = getattr(props, name)
    str_repr = str(obj)

    # Failure.
    if str_repr != repr:
        raise NameError("The string representation of props.%s is %s but it should be %s." % (name, str(str_repr), str(repr)))

    # Test passed.
    print("The string representation of props.%s is '%s': Test passed." % (name, str_repr))


def test_underscore_translation(name=None, path=None, value=None):
    """Test the path '-' -> '_' and '__' -> '_' translations.

    @keyword name:      The name of the property tree Python object.
    @type name:         str
    @keyword path:      The expected property tree path.
    @type path:         str
    @keyword value:     The optional value to set the property tree node to (e.g. to create it).
    @type value:        object
    """

    # Get the node.
    node = getattr(props, name)

    # Set the value.
    if value:
        setattr(props, name, value)

    # Print and check the path.
    print(repr(node))
    node_path = node.strPath()
    if node_path != path:
        raise NameError("The paths '%s' and '%s' do not match." % node_path, path)


def title(text):
    """Format the titles for each test category.

    @param text:    The text of the title.
    @type text:     str
    """

    top = "#" * (len(text) + 4)
    print("\n\n%s" % top)
    print("# %s #" % text)
    print("%s\n" % top)


print("\n" + "*"*80)
print("This is the py-ogel, test.py external python script.")

title("Check out the property tree module.")
print("Importing prop_tree.")
import prop_tree
print("prop_tree.__dict__ = %s" % dir(prop_tree))
print("prop_tree.Props.__dict__ = %s" % dir(prop_tree.Props))
print("prop_tree.Node.__dict__ = %s" % dir(prop_tree.Node))
#print("props.__dict__ = %s" % dir(props))
del prop_tree

title("Testing some properties.")
print("%-20s %s" % ("props.sim: ", repr(props.sim)))
x = props.sim.aero
print("%-20s %s" % ("x:", x))
print("%-20s %s" % ("x.strPath(): ", x.strPath()))
y = props.systems.electrical.serviceable
print("%-20s %s" % ("x: ", x))
print("%-20s %s" % ("y: ", y))
print("%-20s %s" % ("x.strPath(): ", x.strPath()))
print("%-20s %s" % ("y.strPath(): ", y.strPath()))
print("%-20s %s" % ("repr(x): ", repr(x)))
print("%-20s %s" % ("repr(y): ", repr(y)))

title("Testing deletion of an aliased node.")
del x

title("Testing property setting.")
props.environment.moonlight = 0.3
z = props.environment.moonlight
print("%-20s %s" % ("z: ", repr(z)))
print("%-20s %s" % ("z: ", repr(z)))
z = props.environment.moonlight[0]
props.environment.moonlight[0] = 20
print("%-20s %s" % ("z: ", repr(z)))
print(repr(props.systems.electrical.serviceable))
props.systems.electrical.serviceable = False
print(repr(props.systems.electrical.serviceable))
props.systems.electrical.serviceable = True
print(repr(props.systems.electrical.serviceable))
props.environment.aaa = "test string"
print(repr(props.environment.aaa))
props.environment.testint = 100
print(repr(props.environment.testint))

title("Testing concatenation.")
data = [["a", "b", "ab"], [1, 2, 3], [1.0, 2.0, 3.0]]
for i in range(len(data)):
    print("\nSet %i: %s" % (i, data[i]))
    props.py_testing[i].a = data[i][0]
    props.py_testing[i].b = data[i][1]
    a = props.py_testing[i].a
    b = props.py_testing[i].b
    props.py_testing[i].c = (a + b)
    print("\tTrue result: %s" % (a + b))
    print("\tProperty tree result: %s" % repr(props.py_testing[i].c))
    if props.py_testing[i].c != data[i][2]:
        str = "\tThe results do not match: %s != %s" % (repr(props.py_testing[i].c), repr(data[i][2]))
        raise NameError(str)
    else:
        print("\tThe results match.")

title("Testing property setting failure.")
try:
    props.environment.testint = None
except AttributeError:
    print("Skipping the AttributeError.")

title("Testing maths operations.")
print("z = %s" % repr(z))
print("z + 1  = %s" % (z + 1))
print("1 + z  = %s" % (1.0 + z))
print("z - 1  = %s" % (z - 1.0))
print("1 - z  = %s" % (1 - z))
print("z * 2  = %s" % (z * 2.0))
print("2 * z  = %s" % (2.0 * z))
print("z / 3  = %s" % (z / 3.0))
print("3 / z  = %s" % (3.0 / z))
print("z**2   = %s" % (z**2))
print("2**z   = %s" % (2**z))
print("z %% 3  = %s" % (z % 3))
print("3 %% z  = %s" % (3 % z))
print("z // 3 = %s" % (z // 3))
print("3 // z = %s" % (3 // z))
props.test_maths[0] = -3
z = props.test_maths[0]
print("\nz = %s" % repr(z))
print("z / 2 = %s" % (z / 2.0))
print("2 / z = %s" % (2.0 / z))

title("Testing invalid maths operations.")
props.invalid_math.type[0] = "X"
print(repr(props.invalid_math.type[0]))
invalid_math_check(node=props.environment.aaa, type="<str>")
props.invalid_math.type[1] = True
print(repr(props.invalid_math.type[1]))
invalid_math_check(node=props.environment.aaa, type="<bool>")

title("Testing the non-existant path '/abc' for an AttributeError.")
try:
    print(repr(props.abc))
    raise NameError("No AttributeError has been raised.")
except AttributeError:
    print("AttributeError for props.abc correctly raised.")


title("Testing path '-' and '_' translations.")
test_underscore_translation(name="position.altitude_ft", path="/position/altitude-ft")
test_underscore_translation(name="underscore.a_b__c_d__e", path="/underscore/a-b_c-d_e", value="underscore test")


title("Testing the length of an array.")
test_length(name="py_testing", length=len(data))
test_length(name="systems.electrical.serviceable", length=1)


title("Testing setattr() and hasattr() on the props object.")
setattr(props, 'setattr_test', True)
print(repr(props.setattr_test))
if not hasattr(props, 'setattr_test'):
    raise NameError("The \"/setattr-test\" property node was not created.")


title("Equality condition testing.")
test_equality(name="test_bool_equality", value=True, eq=True, ne=False)
test_equality(name="test_int_equality", value=10, eq=10, ne=True, le=[10, 21], ge=[10, 1], lt=20000, gt=-2000)
test_equality(name="test_double_equality", value=10.0, eq=10.0, ne=True, le=[10.0, 21.0], ge=[10.0, 1.0], lt=20000.0, gt=-2000.0)
test_equality(name="test_string_equality", value="hello", eq="hello", ne="Hello")
try:
    print("Segfault checking:")
    test_equality(name="test_string_equality_segfault", value="hello", eq="hello", ne="Hello", le=[10.0, 21.0], ge=[10.0, 1.0], lt=20000.0, gt=-2000.0)
except NameError:
    print("\nNameError caught - no segfault.")


title("Testing the string representation.")
test_string_repr(name="test_string_repr", value='Hello!', repr=None)
test_string_repr(name="test_string_repr[1]", value=200, repr='200')
test_string_repr(name="test_string_repr[2]", value=True, repr='True')


title("Subnode testing.")
print("Normal subnode.")
props.test_subnode.c = "subnode"
print("\tSetting: a = props.test_subnode")
a = props.test_subnode
print("\ta.c: %s" % repr(a.c))
print("\tSetting: b = props.test_subnode.c; b += '_test'")
b = props.test_subnode.c
b += '_test'
print("\tSetting: c = a.c")
c = a.c
print("\ta: %s" % repr(a))
print("\tb: %s" % repr(b))
print("\tc: %s" % repr(c))
if a.c != "subnode_test":
    raise NameError("\tThe test_subnode.c value of '%s' should be 'subnode_test'." % a.c)

print("Array-type subnode.")
props.test_subnode[1].c = "subnode"
print("\tSetting: a = props.test_subnode[1]")
a = props.test_subnode[1]
print("\ta.c: %s" % repr(a.c))
print("\tSetting: b = props.test_subnode[1].c; b += '_test'")
b = props.test_subnode[1].c
b += '_test'
print("\tSetting: c = a.c")
c = a.c
print("\ta: %s" % repr(a))
print("\tb: %s" % repr(b))
print("\tc: %s" % repr(c))
if a.c != "subnode_test":
    raise NameError("\tThe test_subnode[0].c value of '%s' should be 'subnode_test'." % a.c)


title("Testing inplace maths operations.")
props.test_inplace[0] = 20
z = props.test_inplace[0]; print("Init z  = %s" % repr(z))
z += 1;  print("z += 1  = %s" % repr(z))
z -= 11; print("z -= 11 = %s" % repr(z))
z *= 2;  print("z *= 2  = %s" % repr(z))
z /= 3;  print("z /= 3  = %s" % repr(z))
z **= 2; print("z **= 2 = %s" % repr(z))
z //= 3; print("z //= 3 = %s" % repr(z))
z %= 3;  print("z %%= 3  = %s" % repr(z))

props.test_inplace[1] = 20.0
z = props.test_inplace[1]; print("\nInit z  = %s" % repr(z))
z += 1;  print("z += 1  = %s" % repr(z))
z -= 11; print("z -= 11 = %s" % repr(z))
z *= 2;  print("z *= 2  = %s" % repr(z))
z /= 3;  print("z /= 3  = %s" % repr(z))
z **= 2; print("z **= 2 = %s" % repr(z))
z //= 3; print("z //= 3 = %s" % repr(z))
z %= 3;  print("z %%= 3  = %s" % repr(z))

props.test_inplace[2] = "20"
z = props.test_inplace[2]; print("\nInit z   = %s" % repr(z))
z += "1";  print("z += \"1\" = %s" % repr(z))


title("Boolean checks.")
test_bool(title="bool type", name="test_bool_check[0]", value_true=True, value_false=False)
test_bool(title="int type", name="test_bool_check[1]", value_true=1, value_false=0)
test_bool(title="double type", name="test_bool_check[2]", value_true=1.0, value_false=0.0)
test_bool(title="string type", name="test_bool_check[3]", value_true="Hello", value_false="")

print("\n\n" + "*"*80 + "\n")

# Finish with an error.
print("Here is an AttributeError, for luck:")
print(props.does_not_exist)
