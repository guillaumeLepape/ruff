from itertools import starmap
import itertools


# Errors

starmap(func, zip())
starmap(func, zip([]))
starmap(func, zip(*args))

starmap(func, zip(a, b, c,),)


starmap(
    func,  # Foo
    zip(
        # Foo

    )
)

(  # Foo
    itertools
    ) . starmap (

    func,  zip (
        a, b, c,
    ),
)

(  # Foobar
  (  starmap  )
    # Bazqux
) \
(func,
 ( (
     (  # Zip
    (
        (  zip
           # Zip
           )
    )
  )
     (a,  # A
         b,  # B
         c,  # C
   )      )
   ),
)

starmap(
    func \
    , \
    zip \
        (
            a,\
            b,\
            c,\
        )
)


# No errors

starmap(func)
starmap(func, zip(a, b, c, **kwargs))
starmap(func, zip(a, b, c), foo)
starmap(func, zip(a, b, c, lorem=ipsum))
starmap(func, zip(a, b, c), lorem=ipsum)

starmap(func, zip(a, b, c, strict=True))
starmap(func, zip(a, b, c, strict=False))
starmap(func, zip(a, b, c, strict=strict))
