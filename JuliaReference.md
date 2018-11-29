# eNotes on Julia 1.0.2

## Contents

* [Basics](#basics)
  * [Modes](#modes)
  * [Key bindings](#key-bindings)
  * [Notes and conventions](#notes-and-conventions)
  * [Data types](#data-types)
  * [Defining variables](#defining-variables)
    * [Scope of variables](#Scope of variables)
  * Arithmetic
  * Conditionals
  * Loops
* [Array handling](#array-handling)
* Functions
  * Just-in-time compilation
  * Defining functions
    * Restricting function input
  * Using functions and methods
* Environments
  * [Installing & using packages](#Installing & using packages)
  * [Packages worth examining](#Packages worth examining)
  * [Package RCall and the R mode](#Package RCall and the R mode)
  * [Julia Markdown (.jmd)](#Julia-Markdown-.jmd)

-----

## Basics

* `show(×)`: like `echo x` or `print(×)`. `

* `@show a`: 

* `less`: To see the Julia code for a function in a package, need to ask for a specific method using the function signature, tuple of Types.

  * ```
    methods(sort)
    less(sort, (AbstractArray{Int,1},)) # function name, tuple of argument types
    @less sort([7,2,8]) # same result as above
    ```

    This last line opens the viewer "less" to view the file where the code is defined, for the particular function on the particular types of input. also shows file name & path.

    ```
    typeof(10:-1:1)
    less(sort, (StepRange,)) # StepRange is an AbstractRange
    @less sort(10:-1:1)      # same thing
    ```

* 

### Modes

* Help mode: `?`
* Shell mode: `;`
* Package mode: `]`
* R mode: `$` (uses RCall package)
* Hit backspace to go back to Julian mode (the main mode).

###Key bindings

* `^D`: exit
* `^C`: interrupt/cancel (also goes back to Julian mode from Help, Shell, Package, or R mode)

### Notes and conventions

* Julia is 1-indexed (like R, unlike Python).
* Functions that end in exclamation points (e.g. `push!(a)`) will modify their arguments.
* Functions that start in `@` (e.g. `@show x`) **[DO WHAT EXACTLY?]**
* Julia is very explicit about data types, in part to remind you to check your code and *not to overstep [the limits.](https://docs.julialang.org/en/v1/manual/integers-and-floating-point-numbers/)* If you're using `Int64`, for instance, you can't code any number larger than 2^63 - 1 or smaller than 2^-63.



### LaTeX characters

| To get this... | ...type this, then TAB                      |
| -------------- | ------------------------------------------- |
| ≈              | \approx                                     |
| σ              | \sigma (this works for other Greek letters) |
|                |                                             |
|                |                                             |
|                |                                             |
|                |                                             |
|                |                                             |
|                |                                             |
|                |                                             |

### Data types

* Data types:
  * Booleans: `Bool`
  * `String` (in double quotes) and `Char` (in single quotes)
  * Floating-point numbers: `Float16`, `Float 32`, `Float64`; `Float` depends on the machine. The number is how many bits are used to store it.
  * Integers: `Int8`, `Int16`, `Int32`, `Int64`, etc. Again, depends on the machine. If you're on a 64-bit machine, use `Int64`.
  * Unsigned (positive) integers: `UInt8` etc. (This saves a bit: when you don't have to specify +/-, that's one more bit for storing number value)
  * Arrays: rather like Python's lists. Can be multidimensional. By default, contains a single data type, which is defined when the array is created. (`Any` is a valid "type" for arrays though; it's auto-selected for arrays created with multiple types. More flexible, but more computationally expensive.)
  * Tuples: like in Python (e.g. `(3,)` or `(3, "hohoho")` )
  * Vector (Matrix): shortcut for 1D (2D) array
  * Dictionaries: `Dict`
* Special types:
  * Missing: `Missing`, like R's `NA`.
  * Union types: e.g. type `Union{Missing, Int}` can contain integers AND/OR missing values.
  * "Any" type: `Any`, union of all the types. Auto-selected for arrays created with multiple types. More flexible, but more computationally expensive.
  * Symbols: anything that starts with a colon, e.g. `:symbol`. Symbols are immutable and are never garbage-collected. (They're also hashed so it's very fast to look them up; strings are not, so it takes much longer.)
    * Column names in data frames are symbols.
    * `String(:whatever)` converts symbols into strings; `Symbol("whatever")` does the opposite.
* Abstract types:
  * Used to define broader classes. In Julia, *all* data types are effectively classes, 
     and all functions are methods from those classes.
  * [Here's the type hierarchy.](https://commons.wikimedia.org/wiki/File:Type-hierarchy-for-julia-numbers.png) 
     (from [this book](https://en.wikibooks.org/wiki/Introducing_Julia/Types#Type_hierarchy))
  * `Int64 <:` return the larger abstract type, `Integer`, of which `Int64` is a type.
  * `Int64 <: Integer`: "Is `Int64` part of the supertype Integer?"
  * `supertype(Integer)`: "What is the supertype of `Integer`?" (It's `Real`.)
  * All objects must have concrete types (i.e. one at the lowest level of the hierarchy).
* Mutable & immutable types
  * Mutable: arrays, composite types (usually)
  * Immutable: numbers (ints, floats), tuples, strings
  * (When defining a dictionary, the keys must be immutable.)
* `typeof(×)`: returns the data type of `x`.
* `isa(3, Int)`: returns the boolean for whether `3` is an integer, i.e. a member of the 
  abstract type `Integer`. Would also return `True` for `(3, Int64)`, `(3,Real)`,
  `(3,Signed)`, etc.
* `convert(Type, x)`: creates a new object that is a copy of `x` except that it's of type 
  `Type`.
* `typemax(Int)`: returns the largest integer your system can code for

### Defining variables

* Int: `a = 5`
  * `UInt8(10)`: Code the value `10` into unsigned integers. Note that the output is in 
    hexadecimal. `0x0a` says that the first nibble (4 bits) is 0, the second is 10.
* String / character: `a = "horse"`, `a = 'fish'`
* Array: `a = [1, 1, 2, 3, 5, 8]`
  * `Vector{Int}`: "Vector" is shorthand for a 1-dimensional array.  (This command returns 
    `Array{Int64,1}` -- the type designation for a 1-D array of 64-bit integers.)
    * Vectors in Julia have no direction -- they aren't horizontal or vertical. To specify 
      that, instead use a matrix with (e.g.) one row and many columns.
  * Multidimensional arrays: `a = [1 2 3 ; 6 7 8]`. Spaces separate columns, semicolons 
    separate rows.
* Dictionary: `h = Dict("blue"=>10, "green"=>20)`
* You can define variables without initializing them / giving them values: 
  `a = Array{Int8,2}(undef, 3,4)`
* `similar(×)`: Find an unallocated bit of memory to hold the same data type as `x`, e.g. 
  if `x` is a 3x4 array, then another 3x4 array.
* `zeros(3)`: Gets space for a 3-element array and initializes the whole thing to zeros. 
  Similar behavior for `ones(3)`.
  * Try `ones(Bool, 3)` and/or `zeros(Bool, (3,2))`

#### Scope of variables

**Global scope:** inside the main session. **Local scope:** anything inside `for` loops, `while` loops, functions, `try`s, etc.

Julia dislikes changing values in the global scope. Local scopes can't modify 



### Arithmetic

* `x += 1`: increment `x` by 1
* `10:-1:1`: series of numbers from 10 to [] by []s
* 

-----

## Scripting

* `error("message")`: Quit the current function. This is fatal.
  * `@error "message"`: Show a big warning, but don't quit the function.
  * `@warn "message"`: Show this message, also without quitting.
  * `@info "message" x b`: Show "message", then show the values of `x` and `b`. Very handy for debugging. (`@error` and `@warn` will do this too.)
  * `@debug "message"`: Function not stopped. Messages not shown unless requested with a different function. Very useful for developers.

### Conditionals

* `x || y`: `x` or `y`
* `x && y`: `x` and `y`
* `x == y`: `x` equals `y`. (Not good for floats!)
* `x ≈ y` (typed "\approx" + TAB, as per LaTeX): `x` is approximately equal to `y`. Good for checking equality between floating-point values.
  * Alternately, `isapprox(x,y)`, but that's clumsier to read.
* 

```Julia
x=5; y=6.2
if x>6 || y>6
  println("x or y is >6")
end
x>6 || error("x is not greater than 6: can't continue")
x>6 || @error "oops, x<=6. error, but not fatal (under standard logging level)"
x>6 || @warn "oops, x not >6, is this normal?"
x<6 && @info "checked: x is less than 6"
x<6 && @debug "message to help debug: x is less than 6"

function test(x,y)
  if x ≈ y # type \approx then TAB. Same as isapprox(x,y).
    relation = "(approx) equal to"
  elseif x < y
    relation = "less than"
  else
    relation = "greater than"
  end
  println(x, " is ", relation, " ", y, ".")
end
test(x,y)
1.1+0.1 == 1.2
test(1.1+0.1, 1.2)

isxbig = x>3 ? "yes" : "no"   # ternary expression: very short if/else
isxbig = (x>3 ? "yes" : "no") # same
isxbig = x>3 # don't do (test ? true : false)
```

### Loops

```Julia
for i in 1:10^9 # this is a Range object, and thus much smaller than an actual list of all 10^9 numbers
  println("i=",i)
  if i<3
    continue
  end
  # above, same as: i<3 && continue
  println("\t2i=", 2i) # * not needed
  i<6 || break
end
i # not defined!!
```



##Array handling

* `a[1]`: Return the first element of `a`.
  * Note that Julia is 1-indexed (like R, unlike Python)
* `sort(a)`:  Return the elements of `a`, sorted.
  * `sort!(a)`: Sort `a` (and save it that way), then return its elements in their new 
    order.
  * A convention: functions that end in exclamation points (e.g. `push!(a)`) will modify
    their arguments.
* `push!(a,5)`: adds element `5` to the array `a`. Note that if you try to push an element
  of a type other than the array contains, Julia will convert it if possible (e.g., 
  pushing `5.0` to an `int64` array will instead push `5`, but pushing `5.1` will throw an 
  error because it doesn't convert cleanly.)
* `pop!(a)`: Return the last element of `a`, then remove that element from `a`.

-----

## Functions

###Just-in-time compilation

You won't see this -- it's all behind the scenes -- but functions aren't compiled until 
you actually try to use them. (Thus, the first time you try to use a function, it'll be a 
lot slower than in later uses.)

### Defining functions

```{julia}
function addone(x)
  return x+1
end
```

* There's also a one-line form: `addone(x) = x+1`
* `code_llvm(addone, (Int,))`: Examine, in detail, the code generated when you compiled 
  `addone()`. Note that it'll be different for different data types.
* Use a dot to apply functions across vectors -- Julia is really good at this.
  * `addone.([1,2,7,9])`: Applies our `addone` function to the vector `[1,2,7,9]` and 
    outputs `[2,3,8,10]`.
  * This works with basic functions, too: `[1,5,9] .+ 3` returns `[4, 8, 12]`.
  * `log([1,2,3,4,5])` throws an error, but `log.([1,2,3,4,5])` doesn't. Mustn't forget 
    the dot.
* `methods(addone)`: lists all the methods found in `addone`.

#### Docstrings

They go *just* before the function:

```Julia
"""
foo(x)

calculate x+1
"""
function foo(x)
  return x+1
end
?foo
```

#### Restricting function input

```{julia}
function addone(x::Number) # The double colon specifies that x MUST be a number.
  return x+1
end
```

A better way:

```{Julia}
function addone(x) # no type declaration. re-defining
  return x+one(x)  # one(x) = (additive?) identity element for * of same type as x
end
```

That function will work on a much wider range of inputs.

If you've already declared the above, and then do this:

```{Julia}
function addone(x::String)
  return x * " one"
end
```

...then you've just added another method to the function `addone`. It can now handle numbers, arrays, AND strings.

### Using functions and methods

* `methods(sort)`: show all the methods for function `sort`.

-----

# Environments

A Julia environment defines the version of Julia you're using and the packages loaded in. You can create an environment in an empty folder by doing, e.g., the following (see class notes for the version with output) from within the folder where you want the new environment:

```{julia}
(v1.0) pkg> activate .
(juliaenv) pkg> status
(juliaenv) pkg> add MixedModels
(juliaenv) pkg> status
(juliaenv) pkg> status --manifest
```

Later, you can use the environment defined in this folder by providing the path with `activate`:

```{Julia}
v1.0) pkg> activate st679/juliaenv

(juliaenv) pkg> status
    Status `~/Documents/private/st679/juliaenv/Project.toml`
  [ff71e718] MixedModels v1.1.1

julia> using MixedModels
[ Info: Precompiling MixedModels [ff71e718-51f3-5ec2-a782-8ffcbfa3c316]
```

###Installing & using packages

You install packages once per environment, but use them every time you start up.

* Install them in package mode: `add PackageName`
* Then, in Julian mode, load them into memory: `using PackageName`

### Packages worth examining

* [StatsPlots](https://github.com/JuliaPlots/StatPlots.jl)
* [GGPlots](https://github.com/JuliaPlots/GGPlots.jl)
* [Interact](https://github.com/JuliaGizmos/Interact.jl): adds interactive widgets to plots, so you can adjust, e.g., number of bins in a histogram, *on the fly*
* [PyCall](https://github.com/JuliaPy/PyCall.jl): as RCall, but for Python

### Package RCall and the R mode

A terribly useful package that lets you jump between R and Julia, with both languages sharing the same data. Cécile mostly uses it to do calculations in Julia and then plot the data in R (she's not very satisfied with Julia's plotting packages). This certainly isn't *faster* than RStudio, but if you're already in Julia and want some R functionality, it's perfect for that.

* `$`: gets you into R mode (after `using RCall`)
* `$a`: from R mode, grabs the value of variable `a` from the Julia session's memory
  * Julia variables show up in `ls()` as `#JL` -- "something that belongs in Julia".
* `R"b"`: from Julian mode, execute the string "b" as an R command (in this case, e.g., print the value of the R variable `b`). There's no extra memory used: Julia has a pointer to the R object.
* `@rget b`: from Julian mode, grab the value of variable `b` from the R session's memory and save it as a Julia variable by the same name.
  * `@rget(b)`: in Julian mode, refer to variable B in the R session's memory (e.g. `a + @rget(b)`).

### Julia Markdown (.jmd)

Rough equivalent of R Markdown -- can execute blocks of Julia code within Markdown document.













.