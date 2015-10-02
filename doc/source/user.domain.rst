Fortran extension to :mod:`sphinx.domains`
==========================================

The module :mod:`sphinxfortran.fortran_domain` 
is an extension to Sphinx adding the FORTRAN "domain"  (see 
the :sphinx:`sphinx documentation<domains.html>` on syntactic domains),
and can therefore document FORTRAN codes.

.. highlight:: rst

Configurer Sphinx
-----------------

Just add :mod:`sphinxfortran.fortran_domain`
to the list defined by the :attr:`extension` variable in the file
:file:`conf.py` sphinx configuration file
(assuming the :mod:`vacumm` python package is available to you).

Syntax
------

This extension provides "guidelines" to declare (describe and reference) 
fortran entities (program, module, type, function, subroutine and variable), 
as well as "roles" to refer to the declared entities.

Directives
~~~~~~~~~~


All directives are prefixed by ``f:`` to refer to the fortran domain.

.. note::
    
    Thereafter, the brackets ``[]`` denote an optional argument.
    
All directives accept content to describe the entity, which will interpreted by sphinx.
This description can also take advantage of
:ref:`docfields <docfields>`
to describe the arguments of functions, subroutines and programs.

.. rst:directive:: .. f:program:: progname

    Description of a FORTRAN program. 
    This directive accepts :ref:`docfields <docfields>`.   
    
    Example::
        
        .. f:program:: main
            
            This is the main program.
    
    
.. rst:directive:: .. f:module:: modname

    This creates a reference to a module and produces no output. 
    It accepts the ``:synopsis:`` option to briefly 
    describe the module in the modules index.
    It also defines the current module,
    like :rst:dir:`f:currentmodule`.
    
    Example::
        
        .. f:module:: monmodule
            :synopsis: Statistics module
                
    
.. rst:directive:: .. f:currentmodule:: [modname]

    This directive produces no output, it makes of ``modname``
    the current module:
    functions, subroutines, types and variables 
    described in the following will be considered 
    as belonging to this module. 
    If ``modname`` is empty or equal to ``None``, 
    there is no more current module.
    
    Example::
        
        .. f:currentmodule:: mymodule
        
        .. f:variable:: float myvar
        
        .. f:currentmodule::
            
            
    
.. rst:directive:: .. f:type:: [~][modname][/]typename

    This directive describes a derived type in a module.
    It accepts the special docfield `:f ...:`
    to describe the fields of the module.
    
    Example::
        
        .. f:type:: mymod/mytype
        
            :f integer var1: Variable 1
            :f float var2: Variable 2
    
   
.. rst:directive:: .. f:variable:: [type] [~][modname][/]varname[(shape)]

    This directive describes a variable of a module. 
    It accepts the following options::
    
        - ``:type:``: Type of the variable (``float``, ``mytype``, etc). 
          Si présent, un lien est créé vers ce type. 
          The type can also be specified before the variable name.
        - ``:shape:``: Shape in the form ``nx,ny``,
          which can also be declared after the name (in brackets).
          A reference to all variables found is created.
        - ``:attrs:``: Additional Attributes (``in``, ``parameter``, etc).
        
    Example::
        
        .. f:function:: float myvar
            :shape: nx,ny
            :attrs: in
            
            Description of my variable.
            
    
.. rst:directive:: .. f:function:: [type] [~][modname][/]funcname(signature)

    This directive describes a function belonging or not to a module.
    It accepts the option `:type:` and uses :ref:`docfields <docfields>`
    to describe his arguments, his calls and modules used.
    
    Example::
        
        .. f:function:: myfunc(a [,b])
        
            This is my primary function.
            
            :p float a: My first argument.
            :o integer b [optional]: My second argument.
            :from: :f:subr:`mysub`
   
    
.. rst:directive:: .. f:subroutine:: [~][modname][/]subrname[(signature)]

     This directive describes a subroutine like the directive
     :rst:dir:`f:function`.

    Example::
        
        .. f:subroutine:: mysub(a)
        
            Description.
        
            :param a: My parameter.
            :to: :f:func:`myfunc`
    
The roles
~~~~~~~~~

The roles allow in rst language to refer to entities (program, function, etc.). 
They are used with a syntax like::
    
    :role:`cible`
    :role:`nom <cible>` # avec nom alternatif
    
Several have been defined with respect to fortran guidelines presented above.

.. rst:role:: f:prog

    Reference to a program declared with :rst:dir:`f:program`.

.. rst:role:: f:mod:
    
    Reference to a module declared with :rst:dir:`f:module`.
    
.. rst:role:: f:type:
    
    Reference to a derived type declared with :rst:dir:`f:type`.
    
.. rst:role:: f:var:
    
    Reference to a variable declared with :rst:dir:`f:variable`.

.. rst:role:: f:func

    Reference to a fonction or a subroutine declared 
    respectively with :rst:dir:`f:function` and :rst:dir:`f:subroutine`.

.. rst:role:: f:subr:
    
    Alias for :rst:role:`f:func`.
    

It is possible to make reference to derived types, variables, 
functions and subroutines belonging to a module, with the typical following syntax:
    
    :f:func:`monmodule/myfunction`
    
If a local function and the module have the same name, 
it is possible to use the following syntax if the current 
module is the same as the function module:
    
    :f:func:`/myfunction`
    
If the / is omitted, the reference will focus on the local function and not that of the current module.

If the module is specified in the reference, it is possible not to display the name by prefixing 
``"~"``::
    
    :f:func:`~mymodule/myfunction`
    
.. _docfields: 

The *docfields*
~~~~~~~~~~~~~~~

The docfields are rst tags of type
:rstdoc:`field list <restructuredtext.html#field-lists>`,
which are interpreted in the content of certain directives 
to describe the settings, options and other special fields.
 
The fortran domain allows a use pretty close to
:sphinx:`that implemented <domains.html#info-field-lists>` 
for the :sphinx:`python domain <domains.html#the-python-domain>`.

There are two families of fortran *docfields*: 
one for functions and subroutines, and one for derived types.


.. rubric:: Fonctions et subroutines family

For this family, the *docfields* are used to describe 
the mandatory and optional arguments, the modules used, 
the programs, functions and subroutines that call the current entity, 
and the functions and subroutines called by this entity.
Some of them have aliases.

- ``param`` (or ``p``, ``parameter``, ``a``, ``arg``, ``argument``): Mandatory argument. ::
    
    :param myvar: Description.
    
  It is possible to specify the type, the size and special attributes 
  in the declaration following the example below:
      
      :param mytype myvar(nx,ny) [in]: Description.
       
- ``type`` (or ``paramtype``, ``ptype``): Parameter type (eg: float). 
  Reference is made to this parameter if present. ::
    
    :type: float
    
- ``shape`` (ort ``pshape``): Shape of the parameter (dimensions are separated by commas).

    :shape: nx, ny
    
- ``attrs`` (or ``pattrs``, ``attr``): Special Attributes (separated by commas). ::
    
    :attr: in/out
    
- ``option`` (or ``o``, ``optional``, ``keyword``): Declaration of an optional parameter with a similar syntax to required parameters (``param``).
- ``otype`` (or ``optparamtype``): Its type.
- ``oshape`` : Its shape.
- ``oattrs``` (or ``oattrs``): Its attributes.
- ``return`` (or ``r``, ``returns``): Variable returned by the function.
- ``rtype`` (or ``returntype``): Its type.
- ``rshape``: Its shape.
- ``rattrs` (or ``rattrs``): Its attributes.
- ``calledfrom`` (or ``from``): Functions, subroutines or programs calling the current routine.
- ``callto`` (or ``to``): Fonctions ou subroutines called by the current routine.

The **docfiels** are merged into one list for those mandatory,
and another one for those optional,
and their associated **docfiels** (type, dimensions et attributs) are
deleted and inserted in the parameter declaration.

.. note::
    In addition to these *docfiels* that are intepreted, 
    you can add other of your choice. For example::
        
        :actions: This function performs
            
            #) Une initialisation.
            #) Un calcul.
            #) Un plot.
            
        :p float myvar [in]: Variable à tracer.
        :use: Fait appel au module :f:mod:`mymod`.


.. rubric:: Derived types family

These *docfields* describe the fields of derived types.
They are inserted into the header of a :rst:dir:`f:type` directive.

    
- ``ftype`` (or ``f``, typef, typefield): Fields of a derived type with a syntax similar 
  to that of required parameters or routines (``param``).
- ``ftype`` (or ``fieldtype``): Its type.
- ``fshape``: Its shape.
- ``fattrs``` (or ``fattrs``): Its attributes.

Example
-------


.. literalinclude:: user.domain.sample.txt
    :language: rst

 
Which gives:
    
    .. include:: user.domain.sample.txt
    
    
.. note :: 
    Declared modules are listed in their :f:ref:`index <f-modindex>`, 
    and other fortran entities are also accesible from the :ref:`main index <genindex>`.

