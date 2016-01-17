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
            if i == 0:
                print("Correct TypeError: %s + 1" % type)
            elif i == 1:
                print("Correct TypeError: 1 + %s" % type)
            elif i == 2:
                print("Correct TypeError: %s - 1" % type)
            elif i == 3:
                print("Correct TypeError: 1 - %s" % type)
            elif i == 4:
                print("Correct TypeError: %s * 1" % type)
            elif i == 5:
                print("Correct TypeError: 1 * %s" % type)
            elif i == 6:
                print("Correct TypeError: %s / 1" % type)
            elif i == 7:
                print("Correct TypeError: 1 / %s" % type)


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
print("This is the ogel, test.py external python script.")

title("Check out the property tree module.")
print("Importing prop_tree.")
import prop_tree
print("prop_tree.__dict__ = %s" % dir(prop_tree))
print("prop_tree.Props.__dict__ = %s" % dir(prop_tree.Props))
print("prop_tree.Node.__dict__ = %s" % dir(prop_tree.Node))
#print("props.__dict__ = %s" % dir(props))
del prop_tree

title("Testing some properties.")
print("%-20s %s" % ("props.sim: ", props.sim))
x = props.sim.aero
print("%-20s %s" % ("x:", x))
print("%-20s %s" % ("x.strPath(): ", x.strPath()))
y = props.systems.electrical.serviceable
print("%-20s %s" % ("x: ", x))
print("%-20s %s" % ("y: ", y))
print("%-20s %s" % ("x.strPath(): ", x.strPath()))
print("%-20s %s" % ("y.strPath(): ", y.strPath()))

title("Testing deletion of an aliased node.")
del x

title("Testing property setting.")
props.environment.moonlight = 0.3
z = props.environment.moonlight
print("%-20s %s" % ("z: ", z))
print("%-20s %s" % ("z: ", z))
z = props.environment.moonlight[0]
props.environment.moonlight[0] = 20
print("%-20s %s" % ("z: ", z))
print(props.systems.electrical.serviceable)
props.systems.electrical.serviceable = False
print(props.systems.electrical.serviceable)
props.systems.electrical.serviceable = True
print(props.systems.electrical.serviceable)
props.environment.aaa = "test string"
print(props.environment.aaa)
props.environment.testint = 100
print(props.environment.testint)

title("Testing concatenation.")
data = [["a", "b", "ab"], [1, 2, 3], [1.0, 2.0, 3.0]]
for i in range(len(data)):
    print("\nSet %i: %s" % (i, data[i]))
    props.py_testing[i].a = data[i][0]
    props.py_testing[i].b = data[i][1]
    a = props.py_testing[i].a
    b = props.py_testing[i].b
    props.py_testing[i].c = (a + b)
    print("\tresult: %s" % (a + b))
    print("\tresult: %s" % props.py_testing[i].c)
    if props.py_testing[i].c != data[i][2]:
        str = "\tThe results do not match: %s != %s" % (repr(props.py_testing[i].c), repr(data[i][2]))
        print(str)
        #raise NameError(str)

title("Testing property setting failure.")
try:
    props.environment.testint = None
except AttributeError:
    print("Skipping the AttributeError.")

title("Testing maths operations.")
print("z + 1 = %s" % (z + 1))
print("1 + z = %s" % (1.0 + z))
print("z - 1 = %s" % (z - 1.0))
print("1 - z = %s" % (1 - z))
print("z * 2 = %s" % (z * 2.0))
print("2 * z = %s" % (2.0 * z))
print("2 / z = %s" % (2.0 / z))
print("z / 2 = %s" % (z / 2.0))

title("Testing invalid maths operations.")
props.invalid_math.type[0] = "X"
print(props.invalid_math.type[0])
invalid_math_check(node=props.environment.aaa, type="<str>")
props.invalid_math.type[1] = True
print(props.invalid_math.type[1])
invalid_math_check(node=props.environment.aaa, type="<bool>")

title("Testing the non-existant path '/abc' for an AttributeError.")
try:
    props.abc
    raise NameError("No AttributeError has been raised.")
except AttributeError:
    print("AttributeError raised.")

title("Testing 'props.position.altitude_ft' to '/position/altitude-ft' translation.")
print(props.position.altitude_ft)

print("*"*80 + "\n")

# Finish with an error.
print(props.does_not_exist)
