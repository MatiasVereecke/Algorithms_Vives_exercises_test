#Cheatsheet

Python:

```python
one = 1
hi = "hi"
```

C#:

```csharp
int one = 1; 
string hi = "hi"; 
```

## Functions

Python:

```python
# Function definition: takes an argument
def test(number):
  return number + 1


results = test(3)
```

C#:

```csharp
// Function definition: takes an integer argument, returns an integer
static int test(number)
{
  return number + 1;
}

// Function use
var results = test(3);
```

## Conditionals

Python:

```python
if x == 3:
    # ...
elif x == 0:
    # ...
else:
    # ...
```

C#:

```csharp
if (x == 3)
{
  // ...
}
else if (x == 0)
{
  // ...
}
else
{
  // ...
}
```

## Print to screen

Python:

```python
x = 5
print("x has the value %s" % x);
```

C#:

```csharp
var x = 5;
Console.Writeline("x has the value {0}", x);
```
