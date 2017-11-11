# ANSON
ANSON - typed object notation inspired by JSON

## `Rational`

ANSON is a JSON inspired text object notation to make it more strictly-typed as possible.  It makes a great data storage format for any type of data that humans will edit.

- It looks like JSON;
- Supports a lot of standard types include such as numbers, boolean, datetime and strings;
- Has comments using the standard comment convention around;
- No need to quote property name;
- Arrays, Tuples and recursively objects.

## `Example`
```
{
    id: 5643u
    customer: "John Doe"
    sell_datetime: @2017-07-23T12:14:33.079+03:00
    books: [
        {
            id: 52323
            section: ("best sellers", 1)
            title: "Pride and Prejudice"
            date_of_print: #2017-02-01
            has_discount: true
            price: $49.98
        },
        {
            id: 154563
            section: ("literature", "classic", "novels")
            title: "Gone with the Wind"
            date_of_print: #2017-03-01
            has_discount: false            
            price: $19.95
        }
    ]
    total: $69.93   // VAT included
}
```

## `Big example`
```
{
    // it's single line comment
    /* it's block 
    comment */

    some_null: null                         // null value

    int: 1                                  // signed integer
    int: 1u                                 // unsigned integer
    int: u32!5                              // unsigned 32 bit - 5
    int: i64!20_000_000                     // signed 64 bit - 20000000
    float: 5.56                             // float64
    float32: 1.23f                          // float32
    decimal: $249.99                        // decimal

    char: 'c'                               // character
    char_2: '💕'                            // unicode supported
    title: "I'm a string"                   // string
    hello_ru: "Здравствуйте!"               // utf-8
    hello_ch: "你好"
    
    multiline: """multi
        line
        text"""                             // multiline raw string
    multiline2: trim"""
            ABC
            123
            456
        """                                 // trimmed multiline string. Result: "ABC\n123\n456"
    
    // blob is base64 encoded array of bytes
    wiki_slogan: blob"""
        TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0
        aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1
        c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0
        aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdl
        LCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4="""

    some_date: #2017-01-01                  // date
    date_time: #2017-12-31 23:59:59         // datetime
    ts: @2017-02-23T12:14:33.079+03:00      // A timestamp with millisecond precision
    
    bool: true                              // boolean


    // object:
    x: {
        text: "Hello from inner object!"
    }

    // Array is an ordered list of values with the same type
    list: [1, 2, 3]                         // classic JSON array
    some_list: [                            // list of 32 bit float numbers
        1.0f,
        2.5f,
        3.3f,                               // comma is allowed here
    ]

    // Tuple is an ordered list of any values
    tuple: (1, "2", 3.0)                    // tuple of integer, string and float
    some_tuple: (
        $4,
        #2017-05-05,
        true,                               // comma is allowed here
    )

    // list doesn't check struct of tuples and objects:
    list_of_tuples: [(1, 2), ("1", "2", "3")]
    list_of_objects: [
        {
            id: 1
            name: "test"
        },
        {
            title: "Some title"
        }
    ]
}
```
