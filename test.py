# Python module imports.
from operator import pos, neg
from prop_tree import extract_alias, extract_path, extract_type, extract_value, is_alias, is_node
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

# Maths testing index.
MATHS_INDEX = 0


def check_value(val1, val2):
    """Check that the two values are the same.

    @param val1:    The first value.
    @type val1:     object
    @param val2:    The second value.
    @type val2:     object
    """

    # Match.
    if val1 == val2:
        print("The values match, %s == %s." % (repr(val1), repr(val2)))

    # No match.
    else:
        raise NameError("The values do not match, %s == %s." % (repr(val1), repr(val2)))


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


def test_invalid_maths(node=None, type=None):
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


def test_prop_tree_fns(obj=None, result=True):
    """Test if the object is a Node object.

    @keyword obj:       The object to test.
    @type obj:          object
    @keyword result:    The expected result - True if the object is a Node, False otherwise.
    @type result:       bool
    """

    # Printout.
    print("\nChecking %s." % repr(obj))

    # Check.
    answer = is_node(obj)

    # Test the extraction functions.
    if answer:
        print("extract_alias(obj) = %s" % repr(extract_alias(obj)))
        print("extract_path(obj)  = %s" % repr(extract_path(obj)))
        print("extract_type(obj)  = %s" % repr(extract_type(obj)))
        print("extract_value(obj) = %s" % repr(extract_value(obj)))
        print("is_alias(obj)      = %s" % repr(is_alias(obj)))

    # Correct answer.
    if answer == result:
        print("is_node(obj)       = %s" % repr(answer))

    # Failure.
    else:
        raise NameError("is_node(%s) != %s." % (repr(obj), repr(result)))


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

    # Looping test.
    for i in range(len(node)):
        print("Element %i: %s" % (i, repr(node[i])))
        real_path = "/%s[%i]" % (name, i)
        real_path = real_path.replace('__', '=======')
        real_path = real_path.replace('_', '-')
        real_path = real_path.replace('=======', '_')
        real_path = real_path.replace('.', '/')
        if extract_path(node[i]) != real_path:
            raise NameError("The path '%s' should be '%s'." % (extract_path(node[i]), real_path))


def test_maths_operation(val1=None, val2=None, final_val=None, operator=None, error=None, rev=False, inplace=False):
    """Test various maths operators.

    @keyword val1:      The starting value.
    @type val1:         object
    @keyword val2:      The second value in the operation.
    @type val2:         object
    @keyword final_val: The expected value.
    @type final_val:    object
    @keyword operator:  The string representation of the operator.
    @type operator:     str
    @keyword error:     The expected error, if any.  Leave as None for no error expected.
    @type error:        None or ErrorType
    @keyword rev:       A flag which if True will cause the reverse operation to be performed.
    @type rev:          bool
    @keyword inplace:   The flag specifying if the inplace operator should be used.
    @type inplace:      bool
    """

    # Init.
    error_flag = False
    global MATHS_INDEX
    op_val = [None, None]
    args = 1
    if val2 != None and not inplace:
        args = 2

    # Sanity check.
    if rev and inplace:
        raise NameError("Testing the reverse inplace operation is not supported.")

    # Forwards operation, with error catching.
    try:
        # Loop over two conditions - [Node + PyObject, Node + Node].
        for i in range(args):
            # Node + PyObject - set the initial value, and alias it.
            if i == 0:
                props.test_inplace[MATHS_INDEX] = val1
                a = props.test_inplace[MATHS_INDEX]
                b = val2
                a_repr = repr(a)
                a_text = "<node>"
                b_repr = repr(b)
                b_text = b_repr
                MATHS_INDEX += 1
            else:
                props.test_inplace[MATHS_INDEX] = val2
                b = props.test_inplace[MATHS_INDEX]
                b_repr = repr(b)
                MATHS_INDEX += 1

            # Switch the values.
            if rev:
                tmp1, tmp2 = b, a
            else:
                tmp1, tmp2 = a, b

            if operator == '+':
                if not inplace:
                    op_val[i] = tmp1 + tmp2
                else:
                    tmp1 += tmp2
            elif operator == '-':
                if not inplace:
                    op_val[i] = tmp1 - tmp2
                else:
                    tmp1 -= tmp2
            elif operator == '*':
                if not inplace:
                    op_val[i] = tmp1 * tmp2
                else:
                    tmp1 *= tmp2
            elif operator == '/':
                if not inplace:
                    op_val[i] = tmp1 / tmp2
                else:
                    tmp1 /= tmp2
            elif operator == '**':
                if not inplace:
                    op_val[i] = tmp1 ** tmp2
                else:
                    tmp1 **= tmp2
            elif operator == '%':
                if not inplace:
                    op_val[i] = tmp1 % tmp2
                else:
                    tmp1 %= tmp2
            elif operator == '//':
                if not inplace:
                    op_val[i] = tmp1 // tmp2
                else:
                    tmp1 //= tmp2
            elif operator == 'divmod':
                if not inplace:
                    op_val[i] = divmod(tmp1, tmp2)
                else:
                    raise NameError("Inplace not supported.")
            elif operator == 'neg':
                if inplace or rev:
                    raise NameError("Inplace or reverse operations are not supported.")
                op_val[i] = neg(a)
            elif operator == 'pos':
                if inplace or rev:
                    raise NameError("Inplace or reverse operations are not supported.")
                op_val[i] = pos(a)
            elif operator == 'abs':
                if inplace or rev:
                    raise NameError("Inplace or reverse operations are not supported.")
                op_val[i] = abs(a)
            elif operator == '~':
                if inplace or rev:
                    raise NameError("Inplace or reverse operations are not supported.")
                op_val[i] = ~a
            elif operator == '<<':
                if not inplace:
                    op_val[i] = tmp1 << tmp2
                else:
                    tmp1 <<= tmp2
            elif operator == '>>':
                if not inplace:
                    op_val[i] = tmp1 >> tmp2
                else:
                    tmp1 >>= tmp2
            elif operator == '&':
                if not inplace:
                    op_val[i] = tmp1 & tmp2
                else:
                    tmp1 &= tmp2
            elif operator == '^':
                if not inplace:
                    op_val[i] = tmp1 ^ tmp2
                else:
                    tmp1 ^= tmp2
            elif operator == '|':
                if not inplace:
                    op_val[i] = tmp1 | tmp2
                else:
                    tmp1 |= tmp2

            elif operator == 'int':
                if inplace or rev:
                    raise NameError("Inplace or reverse operations are not supported.")
                op_val[i] = int(a)

            elif operator == 'float':
                if inplace or rev:
                    raise NameError("Inplace or reverse operations are not supported.")
                op_val[i] = float(a)

            # Alias the inplace operation value.
            if inplace:
                op_val[i] = tmp1

    except error:
        error_text = "The %s error was raised as expected." % error
        error_flag = True

    # Printout.
    if operator in ['~', 'abs', 'float', 'int', 'neg', 'pos']:
        op_text = "%s(z)" % operator
    elif operator in ['divmod']:
        if rev:
            op_text = "%s(%s, %s)" % (operator, a_text, b_text)
        else:
            op_text = "%s(%s, %s)" % (operator, b_text, a_text)
    else:
        if rev:
            op_text = "%s %s %s" % (b_text, operator, a_text)
        else:
            op_text = "%s %s %s" % (a_text, operator, b_text)
    if error_flag:
        print("%-20s : %s (From node: %s)" % (op_text, error_text, a_repr))
        return
    else:
        print("%-20s = %-20s (From %s)" % (op_text, op_val[0], a_repr))

    # Test the value.
    if op_val[0] != final_val:
        raise NameError("Node + PyObject: The calculated value %s does not match the expected value %s." % (repr(op_val[0]), repr(final_val)))
    if val2 != None and not inplace and op_val[1] != final_val:
        raise NameError("Node + Node: The calculated value %s does not match the expected value %s." % (repr(op_val[1]), repr(final_val)))

    # Check that the inplace operation did not destroy the node.
    if inplace and not hasattr(op_val[0], '_path'):
        raise NameError("The property tree Node object has been destroyed by the inplace operation, and replaced with '%s'." % repr(op_val[0]))


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
    node_path = extract_path(node)
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
print("%-20s %s" % ("extract_path(x): ", extract_path(x)))
y = props.systems.electrical.serviceable
print("%-20s %s" % ("x: ", x))
print("%-20s %s" % ("y: ", y))
print("%-20s %s" % ("extract_path(x): ", extract_path(x)))
print("%-20s %s" % ("extract_path(y): ", extract_path(y)))
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
print("Type - bool:")
test_maths_operation(val1=True, val2=False, final_val=1,          operator='+')
test_maths_operation(val1=True, val2=False, final_val=1,          operator='+',  rev=True)
test_maths_operation(val1=True, val2=False, final_val=1,          operator='-')
test_maths_operation(val1=True, val2=False, final_val=-1,         operator='-',  rev=True)
test_maths_operation(val1=True, val2=False, final_val=0,          operator='*')
test_maths_operation(val1=True, val2=False, final_val=0,          operator='*',  rev=True)
test_maths_operation(val1=True, val2=False,                       operator='/', error=ZeroDivisionError)
test_maths_operation(val1=True, val2=False, final_val=0.0,        operator='/',  rev=True)
test_maths_operation(val1=True, val2=False, final_val=1,          operator='**')
test_maths_operation(val1=True, val2=False, final_val=0,          operator='**', rev=True)
test_maths_operation(val1=True, val2=False,                       operator='%', error=ZeroDivisionError)
test_maths_operation(val1=True, val2=False, final_val=False,      operator='%',  rev=True)
test_maths_operation(val1=True, val2=False,                       operator='//', error=ZeroDivisionError)
test_maths_operation(val1=True, val2=False, final_val=0,          operator='//', rev=True)
test_maths_operation(val1=True, val2=False,                       operator='divmod', error=ZeroDivisionError)
test_maths_operation(val1=True, val2=False, final_val=(0, False), operator='divmod', rev=True)
test_maths_operation(val1=True,             final_val=-1,         operator='neg')
test_maths_operation(val1=True,             final_val=1,          operator='pos')
test_maths_operation(val1=True,             final_val=1,          operator='abs')
test_maths_operation(val1=True,             final_val=-2,         operator='~')
test_maths_operation(val1=True, val2=False, final_val=1,          operator='<<')
test_maths_operation(val1=True, val2=False, final_val=0,          operator='<<', rev=True)
test_maths_operation(val1=True, val2=False, final_val=1,          operator='>>')
test_maths_operation(val1=True, val2=False, final_val=0,          operator='>>', rev=True)
test_maths_operation(val1=True, val2=False, final_val=False,      operator='&')
test_maths_operation(val1=True, val2=False, final_val=False,      operator='&', rev=True)
test_maths_operation(val1=True, val2=False, final_val=True,       operator='^')
test_maths_operation(val1=True, val2=False, final_val=True,       operator='^', rev=True)
test_maths_operation(val1=True, val2=False, final_val=True,       operator='|')
test_maths_operation(val1=True, val2=False, final_val=True,       operator='|', rev=True)
test_maths_operation(val1=True,             final_val=1,          operator='int')
test_maths_operation(val1=True,             final_val=1.0,        operator='float')

print("\nType - int:")
test_maths_operation(val1=20, val2=1,   final_val=20+1,          operator='+')
test_maths_operation(val1=20, val2=1,   final_val=20+1,          operator='+',  rev=True)
test_maths_operation(val1=20, val2=1,   final_val=20-1,          operator='-')
test_maths_operation(val1=20, val2=1,   final_val=1-20,          operator='-',  rev=True)
test_maths_operation(val1=20, val2=2,   final_val=20*2,          operator='*')
test_maths_operation(val1=20, val2=2,   final_val=20*2,          operator='*',  rev=True)
test_maths_operation(val1=20, val2=3,   final_val=20/3,          operator='/')
test_maths_operation(val1=20, val2=3,   final_val=3/20,          operator='/',  rev=True)
test_maths_operation(val1=5,  val2=2,   final_val=5**2,          operator='**')
test_maths_operation(val1=5,  val2=2,   final_val=2**5,          operator='**', rev=True)
test_maths_operation(val1=24, val2=9,   final_val=24%9,          operator='%')
test_maths_operation(val1=5,  val2=2,   final_val=2%5,           operator='%',  rev=True)
test_maths_operation(val1=20, val2=3,   final_val=20//3,         operator='//')
test_maths_operation(val1=6,  val2=333, final_val=333//6,        operator='//', rev=True)
test_maths_operation(val1=-3, val2=2,   final_val=divmod(-3, 2), operator='divmod')
test_maths_operation(val1=-3, val2=2,   final_val=divmod(2, -3), operator='divmod', rev=True)
test_maths_operation(val1=-3,           final_val=neg(-3),       operator='neg')
test_maths_operation(val1=-3,           final_val=pos(-3),       operator='pos')
test_maths_operation(val1=-3,           final_val=abs(-3),       operator='abs')
test_maths_operation(val1=13,           final_val=~13,           operator='~')
test_maths_operation(val1=13, val2=3,   final_val=13<<3,         operator='<<')
test_maths_operation(val1=13, val2=3,   final_val=3<<13,         operator='<<', rev=True)
test_maths_operation(val1=13, val2=3,   final_val=13>>3,         operator='>>')
test_maths_operation(val1=13, val2=3,   final_val=3>>13,         operator='>>', rev=True)
test_maths_operation(val1=1,  val2=0,   final_val=1&0,           operator='&')
test_maths_operation(val1=1,  val2=0,   final_val=0&1,           operator='&', rev=True)
test_maths_operation(val1=1,  val2=0,   final_val=1^0,           operator='^')
test_maths_operation(val1=1,  val2=0,   final_val=0^1,           operator='^', rev=True)
test_maths_operation(val1=1,  val2=0,   final_val=1|0,           operator='|')
test_maths_operation(val1=1,  val2=0,   final_val=0|1,           operator='|', rev=True)
test_maths_operation(val1=-3,           final_val=-3,            operator='int')
test_maths_operation(val1=-3,           final_val=-3.0,          operator='float')

print("\nType - float:")
test_maths_operation(val1=20.0, val2=1.0,   final_val=20+1,          operator='+')
test_maths_operation(val1=20.0, val2=1.0,   final_val=20+1,          operator='+',  rev=True)
test_maths_operation(val1=20.0, val2=1.0,   final_val=20-1,          operator='-')
test_maths_operation(val1=20.0, val2=1.0,   final_val=1-20,          operator='-',  rev=True)
test_maths_operation(val1=20.0, val2=2.0,   final_val=20*2,          operator='*')
test_maths_operation(val1=20.0, val2=2.0,   final_val=20*2,          operator='*',  rev=True)
test_maths_operation(val1=20.0, val2=3.0,   final_val=20/3,          operator='/')
test_maths_operation(val1=20.0, val2=3.0,   final_val=3/20,          operator='/',  rev=True)
test_maths_operation(val1=5.0,  val2=2.0,   final_val=5**2,          operator='**')
test_maths_operation(val1=5.0,  val2=2.0,   final_val=2**5,          operator='**', rev=True)
test_maths_operation(val1=24.0, val2=9.0,   final_val=24%9,          operator='%')
test_maths_operation(val1=5.0,  val2=2.0,   final_val=2%5,           operator='%',  rev=True)
test_maths_operation(val1=20.0, val2=3.0,   final_val=20//3,         operator='//')
test_maths_operation(val1=6.0,  val2=333.0, final_val=333//6,        operator='//', rev=True)
test_maths_operation(val1=-3.0, val2=2.0,   final_val=divmod(-3, 2), operator='divmod')
test_maths_operation(val1=-3.0, val2=2.0,   final_val=divmod(2, -3), operator='divmod', rev=True)
test_maths_operation(val1=-3.0,             final_val=neg(-3),       operator='neg')
test_maths_operation(val1=-3.0,             final_val=pos(-3),       operator='pos')
test_maths_operation(val1=-3.0,             final_val=abs(-3),       operator='abs')
test_maths_operation(val1=13.0,                                      operator='~', error=TypeError)
test_maths_operation(val1=13.0, val2=3.0,                            operator='<<', error=TypeError)
test_maths_operation(val1=13.0, val2=3.0,                            operator='<<', rev=True, error=TypeError)
test_maths_operation(val1=13.0, val2=3.0,                            operator='>>', error=TypeError)
test_maths_operation(val1=13.0, val2=3.0,                            operator='>>', rev=True, error=TypeError)
test_maths_operation(val1=1.0,  val2=0.0,                            operator='&', error=TypeError)
test_maths_operation(val1=1.0,  val2=0.0,                            operator='&', rev=True, error=TypeError)
test_maths_operation(val1=1.0,  val2=0.0,                            operator='^', error=TypeError)
test_maths_operation(val1=1.0,  val2=0.0,                            operator='^', rev=True, error=TypeError)
test_maths_operation(val1=1.0,  val2=0.0,                            operator='|', error=TypeError)
test_maths_operation(val1=1.0,  val2=0.0,                            operator='|', rev=True, error=TypeError)
test_maths_operation(val1=-3.0,             final_val=-3,            operator='int')
test_maths_operation(val1=-3.0,             final_val=-3.0,          operator='float')

print("\nType - str:")
test_maths_operation(val1="20", val2="1", final_val="201", operator='+')
test_maths_operation(val1="20", val2="1", final_val="120", operator='+',  rev=True)
test_maths_operation(val1="20", val2="1",                  operator='-', error=TypeError)
test_maths_operation(val1="20", val2="1",                  operator='-',  rev=True, error=TypeError)
test_maths_operation(val1="20", val2="2",                  operator='*', error=TypeError)
test_maths_operation(val1="20", val2="2",                  operator='*',  rev=True, error=TypeError)
test_maths_operation(val1="20", val2="3",                  operator='/', error=TypeError)
test_maths_operation(val1="20", val2="3",                  operator='/',  rev=True, error=TypeError)
test_maths_operation(val1="5",  val2="2",                  operator='**', error=TypeError)
test_maths_operation(val1="5",  val2="2",                  operator='**', rev=True, error=TypeError)
test_maths_operation(val1="24", val2="9",                  operator='%', error=TypeError)
test_maths_operation(val1="5",  val2="2",                  operator='%',  rev=True, error=TypeError)
test_maths_operation(val1="20", val2="3",                  operator='//', error=TypeError)
test_maths_operation(val1="6",  val2="3",                  operator='//', rev=True, error=TypeError)
test_maths_operation(val1="-3", val2="2",                  operator='divmod', error=TypeError)
test_maths_operation(val1="-3", val2="2",                  operator='divmod', rev=True, error=TypeError)
test_maths_operation(val1="-3",                            operator='neg', error=TypeError)
test_maths_operation(val1="-3",                            operator='pos', error=TypeError)
test_maths_operation(val1="-3",                            operator='abs', error=TypeError)
test_maths_operation(val1="13",                            operator='~', error=TypeError)
test_maths_operation(val1="13", val2="3",                  operator='<<', error=TypeError)
test_maths_operation(val1="13", val2="3",                  operator='<<', rev=True, error=TypeError)
test_maths_operation(val1="13", val2="3",                  operator='>>', error=TypeError)
test_maths_operation(val1="13", val2="3",                  operator='>>', rev=True, error=TypeError)
test_maths_operation(val1="1",  val2="0",                  operator='&', error=TypeError)
test_maths_operation(val1="1",  val2="0",                  operator='&', rev=True, error=TypeError)
test_maths_operation(val1="1",  val2="0",                  operator='^', error=TypeError)
test_maths_operation(val1="1",  val2="0",                  operator='^', rev=True, error=TypeError)
test_maths_operation(val1="1",  val2="0",                  operator='|', error=TypeError)
test_maths_operation(val1="1",  val2="0",                  operator='|', rev=True, error=TypeError)
test_maths_operation(val1="-3",           final_val=-3,    operator='int')
test_maths_operation(val1="-3.0",                          operator='int', error=ValueError)
test_maths_operation(val1="-3.0",         final_val=-3.0,  operator='float')
test_maths_operation(val1="abcd",                          operator='int', error=ValueError)
test_maths_operation(val1="abcd",                          operator='float', error=ValueError)


title("Testing invalid maths operations.")
props.invalid_math.type[0] = "X"
print(repr(props.invalid_math.type[0]))
test_invalid_maths(node=props.invalid_math.type[0], type="<str>")


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
print("Type - bool:")
test_maths_operation(val1=True, val2=False, final_val=True,  operator='+',  inplace=True)
test_maths_operation(val1=True, val2=False, final_val=True,  operator='-',  inplace=True)
test_maths_operation(val1=True, val2=False, final_val=False, operator='*',  inplace=True)
test_maths_operation(val1=True, val2=False,                  operator='/',  inplace=True, error=ZeroDivisionError)
test_maths_operation(val1=False, val2=True, final_val=False, operator='/',  inplace=True)
test_maths_operation(val1=True, val2=False, final_val=True,  operator='**', inplace=True)
test_maths_operation(val1=True, val2=False,                  operator='%',  inplace=True, error=ZeroDivisionError)
test_maths_operation(val1=False, val2=True, final_val=False, operator='%',  inplace=True)
test_maths_operation(val1=True, val2=False,                  operator='//', inplace=True, error=ZeroDivisionError)
test_maths_operation(val1=False, val2=True, final_val=False, operator='//', inplace=True)
test_maths_operation(val1=True, val2=False, final_val=True,  operator='<<', inplace=True)
test_maths_operation(val1=True, val2=False, final_val=True,  operator='>>', inplace=True)
test_maths_operation(val1=True, val2=False, final_val=False, operator='&',  inplace=True)
test_maths_operation(val1=True, val2=False, final_val=True,  operator='^',  inplace=True)
test_maths_operation(val1=True, val2=False, final_val=True,  operator='|',  inplace=True)

print("\nType - int:")
test_maths_operation(val1=20, val2=1, final_val=21,  operator='+',  inplace=True)
test_maths_operation(val1=20, val2=1, final_val=19,  operator='-',  inplace=True)
test_maths_operation(val1=20, val2=2, final_val=40,  operator='*',  inplace=True)
test_maths_operation(val1=20, val2=3, final_val=6,   operator='/',  inplace=True)
test_maths_operation(val1=5,  val2=2, final_val=25,  operator='**', inplace=True)
test_maths_operation(val1=24, val2=9, final_val=6,   operator='%',  inplace=True)
test_maths_operation(val1=20, val2=3, final_val=6,   operator='//', inplace=True)
test_maths_operation(val1=13, val2=3, final_val=104, operator='<<', inplace=True)
test_maths_operation(val1=13, val2=3, final_val=1,   operator='>>', inplace=True)
test_maths_operation(val1=1,  val2=0, final_val=0,   operator='&',  inplace=True)
test_maths_operation(val1=1,  val2=0, final_val=1,   operator='^',  inplace=True)
test_maths_operation(val1=1,  val2=0, final_val=1,   operator='|',  inplace=True)

print("\nType - float:")
test_maths_operation(val1=20.0, val2=1.0, final_val=20+1,  operator='+',  inplace=True)
test_maths_operation(val1=20.0, val2=1.0, final_val=20-1,  operator='-',  inplace=True)
test_maths_operation(val1=20.0, val2=2.0, final_val=20*2,  operator='*',  inplace=True)
test_maths_operation(val1=20.0, val2=3.0, final_val=20/3,  operator='/',  inplace=True)
test_maths_operation(val1=5.0,  val2=2.0, final_val=5**2,  operator='**', inplace=True)
test_maths_operation(val1=24.0, val2=9.0, final_val=24%9,  operator='%',  inplace=True)
test_maths_operation(val1=20.0, val2=3.0, final_val=20//3, operator='//', inplace=True)
test_maths_operation(val1=13.0, val2=3.0,                  operator='<<', error=TypeError, inplace=True)
test_maths_operation(val1=13.0, val2=3.0,                  operator='>>', error=TypeError, inplace=True)
test_maths_operation(val1=1.0,  val2=0.0,                  operator='&',  error=TypeError, inplace=True)
test_maths_operation(val1=1.0,  val2=0.0,                  operator='^',  error=TypeError, inplace=True)
test_maths_operation(val1=1.0,  val2=0.0,                  operator='|',  error=TypeError, inplace=True)

print("\nType - str:")
test_maths_operation(val1="20", val2="1", final_val="201", operator='+',  inplace=True)
test_maths_operation(val1="20", val2="1",                  operator='-',  error=TypeError, inplace=True)
test_maths_operation(val1="20", val2="2",                  operator='*',  error=TypeError, inplace=True)
test_maths_operation(val1="20", val2="3",                  operator='/',  error=TypeError, inplace=True)
test_maths_operation(val1="5",  val2="2",                  operator='**', error=TypeError, inplace=True)
test_maths_operation(val1="24", val2="9",                  operator='%',  error=TypeError, inplace=True)
test_maths_operation(val1="20", val2="3",                  operator='//', error=TypeError, inplace=True)
test_maths_operation(val1="13", val2="3",                  operator='<<', error=TypeError, inplace=True)
test_maths_operation(val1="13", val2="3",                  operator='>>', error=TypeError, inplace=True)
test_maths_operation(val1="1",  val2="0",                  operator='&',  error=TypeError, inplace=True)
test_maths_operation(val1="1",  val2="0",                  operator='^',  error=TypeError, inplace=True)
test_maths_operation(val1="1",  val2="0",                  operator='|',  error=TypeError, inplace=True)


title("Boolean checks.")
test_bool(title="bool type", name="test_bool_check[0]", value_true=True, value_false=False)
test_bool(title="int type", name="test_bool_check[1]", value_true=1, value_false=0)
test_bool(title="double type", name="test_bool_check[2]", value_true=1.0, value_false=0.0)
test_bool(title="string type", name="test_bool_check[3]", value_true="Hello", value_false="")


title("Testing indexing.")
props.test_indexing[2] = 10
for i in range(5):
    props.test_indexing[10] = i
props.test_indexing[2].a[2] = "Hello!"
props.test_indexing[10].a[2] = "Hello"
check_value(val1=extract_path(props.test_indexing), val2='/test-indexing')
check_value(val1=extract_path(props.test_indexing[10]), val2='/test-indexing[10]')
check_value(val1=props.test_indexing[2], val2=10)
check_value(val1=props.test_indexing[10], val2=4)
check_value(val1=props.test_indexing[2].a[2], val2='Hello!')
check_value(val1=props.test_indexing[10].a[2], val2='Hello')
props.test_indexing2 = "X"
x = props.test_indexing2
props.test_indexing2[1] = "Y"
y = props.test_indexing2[1]
props.test_indexing2[2] = "Z"
z = props.test_indexing2[2]
check_value(val1=x, val2='X')
check_value(val1=y, val2='Y')
check_value(val1=z, val2='Z')


title("Testing prop_tree functions.")
props.test_node_functions[2] = "Random string"
props.test_node_functions[3] = props.test_node_functions[2]
test_prop_tree_fns(obj=props.test_node_functions[2], result=True)
test_prop_tree_fns(obj=props.test_node_functions[3], result=True)
test_prop_tree_fns(obj=2, result=False)
test_prop_tree_fns(obj="Hello", result=False)
test_prop_tree_fns(obj=object, result=False)
test_prop_tree_fns(obj=props, result=False)
print("\nView the function docs:")
print("\nextract_path.__doc__ = \n\"\"\"\n%s\n\"\"\"" % extract_path.__doc__)
print("\nextract_type.__doc__ = \n\"\"\"\n%s\n\"\"\"" % extract_type.__doc__)
print("\nextract_value.__doc__ = \n\"\"\"\n%s\n\"\"\"" % extract_value.__doc__)
print("\nis_node.__doc__ = \n\"\"\"\n%s\n\"\"\"" % extract_value.__doc__)


title("Testing Node hidden objects.")
props.test_node_hidden = True
a = props.test_node_hidden
print("props.test_node_hidden.__doc__: %s" % repr(a.__doc__))
print("props.test_node_hidden._path: %s" % repr(a._path))
print("extract_path(props.test_node_hidden): %s" % repr(extract_path(a)))


title("Testing a new copy of Props and Node (segfault checks).")
import prop_tree
try:
    new_node = prop_tree.Node()
except Exception:
    pass
new_node = prop_tree.Node(path="test_new_node")
try:
    print("A new Node: %s" % repr(new_node))
except AttributeError:
    pass
props.test_new_node = True
print("A new Node: %s" % repr(new_node))
new_props = prop_tree.Props()
print("A new Props object: %s" % repr(new_props))
print("The new Props object test_new_node Node: %s" % repr(new_props.test_new_node))


title("Test Node aliasing.")
test_vals_orig = ["test", False, -5, 20.0]
test_vals = ["Hop", "", True, False, 1, 0, 1.0, 0.0]
for i in range(len(test_vals_orig)):
    # Loop over the second set of values.
    for j in range(len(test_vals)):
        # Create a starting value, for type checking on overwrite.
        props.test_alias_new[i].iter[j] = test_vals_orig[i]

        # Set the value to be copied.
        props.test_alias[j] = test_vals[j]

        # Alias.
        print("\nSource value:        %s" % repr(test_vals[j]))
        print("Pre-target value:    %s" % repr(test_vals_orig[i]))
        print("Source node:         %s" % repr(props.test_alias[j]))
        print("Pre-target node:     %s" % repr(props.test_alias_new[i].iter[j]))
        props.test_alias_new[i].iter[j] = props.test_alias[j]
        print("Updated target node: %s" % repr(props.test_alias_new[i].iter[j]))

        # Check.
        if props.test_alias_new[i].iter[j] != test_vals[j]:
            raise Exception("The value has not been copied correctly to %s." % repr(props.test_alias_new[i].iter[j]))


print("\n\n" + "*"*80 + "\n")

# Finish with an error.
print("Here is an AttributeError, for luck:")
props.does_not_exist
print(props.does_not_exist)
