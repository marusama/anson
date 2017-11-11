ANSON - typed object notation inspired by JSON
// this format is mostly inspired by JSON
// but it is aimed to support more data types and allowed comments
// file encoding must be utf-8

// it's single line comment
/* it's block 
    comment */
{
    
    // property syntax: <property name>: <optional type!>(<value>|nil)
    // property name: '_', latin letters, digits 0-9
    // name cannot start with digit
    // comma at the end is not allowed
    


    // all properties can have 'null' value (aka nil, None, etc)
    nil_prop: null
    // explicit type
    nil_prop_2: i64! null



    // character represents a single Unicode scalar value
    // character value quoted as '<value>'
    char_1: 'a'
    char_2: '💕'
    // explicit type
    char_3: c!' '



    // simple utf-8 string
    // string value quoted as "<value>"
    // follows C/Java backslash-escape conventions
    string_1: "my test name"
    hello_ru: s!"Здравствуйте"      // explicit type definition also possible
    hello_ch: "你好"                 // chinese Hello
    q: "\""                        // Contains one double-quote character
    uni: "\uABCD"                  // Contains one unicode character    
    naive_multiline: "foo\n bar"   // naive multiline string



    // multiline string
    // quoted as """<value>"""
    multiline: """foo
        bar"""                      // will be equal to "foo\n        bar"



    // trimmed multiline string 
    multiline_tr: trim"""
        Detects a common minimal indent of all the input lines,
        removes it from every line and also removes the first and the last lines
        if they are blank (notice difference blank vs empty).
        Doesn't preserve the original line endings (replaces with LF).
    """
    multiline_tr: trim"""
            ABC
            123
            456
        """ // ABC\n123\n456



    // integer value
    int: -20                            // by default integer is signed number with platform-specific size - int
    int: 20u                            // it's unsigned number with platform-specific size - uint
    int: 20L                            // signed long
    int: 20UL                           // unsigned long
    int: 25_000_000                     // underscore can be used to improve readability
    int: 020                            // octa number
    int: 0x20                           // hexadecimal number
    // type can be specified explicitly
    // possible types: i8, i16, i32, i64, u8, u16, u32, u64
    // not used now, but reserved for future: i128, u128, i256, u256, etc..
    int: i32!-15
    int: u64!33



    // The float type denotes either 32-bit or 64-bit IEEE-754 floating-point values
    // float types: f32 and f64
    // f32 has short notation by adding 'f' at the end of number
    float_1: -3.5                       // by default float is signed 64 float (f64)
    float_1: f64!-3.5                   // the same float with explicit type specified
    float_2: -3.5f                      // 32 bit float
    float_2: f32!-3.5                   // explicit float32 type
    float_nan: nan                      // float64.Nan - Not a number 
    float_nan: NaN                      // it's case insensitive 
    float_pos_infinity: +Infinity       // float64 positive infinite
    float_neg_infinity: -Infinity       // float64 negative infinite



    // Decimal allows accurate representation of base-10 floating point values such as currency amounts.
    // decimal number has type 'd' and has short notation by adding '$' sign at the beginning of number
    decimal: d!150.555222
    decimal: $-0.555222



    // boolean, just boolean
    bool_1: true
    bool_2: false
    bool_1: b!true
    bool_2: b!false



    // Datetime
    // quoted as #<value>
    dt_n: #2017-01-01
    dt_n: #2017-10-59 23:59:59.123
    dt_n: dt!2017-10-59 23:59:59.123



    // Timestamps represent a specific moment in time
    // timestamp has format RFC3339: http://www.ietf.org/rfc/rfc3339.txt
    // quoted as @<value>
    ts_1: @2017-02-23T12:14:33.079+03:00    // A timestamp with millisecond precision and MSK local time
    ts_2: @2017-02-23T20:14:33.079Z         // The same instant in UTC ("zero" or "zulu")
    ts_n: @2017-02-23T20:14:33.079+00:00    // The same instant, with explicit local offset
    ts_n: @2017-02-23T20:14:33.079-00:00    // The same instant, with unknown local offset
    ts_1: ts!2017-02-23T12:14:33.079+03:00  // A timestamp with millisecond precision and MSK local time
    
    
    
    // array is an ordered list of values with the same type
    list: [1, 2, 3]                         // array of integers
    list: u64:[4, 5, 6]                     // type can be declared once for all array
    list: [i32:7, i32:8, i32:9]             // inner type declaration
    list: [7f, 8f, 9f]                      // array of float32
    list: [1, 2, 3,]                        // comma at the end is possible
    list: [1, 2.0, $3]                      // ERROR: it's not allowed to mix types



    // tuple is an ordered list of any values
    tuple_1: (1, 'c', "test", 3.6, $15.2, true)
    tuple_1: (2, -0.33f,)                   // comma at the end is possible



    // object notation
    player: {
        id: 1
        name: "John"
    }



    // list of objects
    list_of_books: [
        {
            id: 1
            title: "Test 1"
            register_date: #2017-01-01
            published: true
            price: $249.99
        },
        {
            id: 2
            title: "Test 2"
            register_date: #2017-02-01
            published: false
            price: $399.98
        },
        {
            id: 3
            title: "Test 3"
            register_date: #2017-03-21
            published: true
            price: $349.98
            updated_at: @2017-02-23T12:14:33.079+03:00
        },                                          // comma at the end is possible
    ]



    // list doesn't check struct of tuples and objects:
    list_of_tuples: [(1, 2), ("1", "2", "3")]   // valid list of tuples
    list_of_objects: [
        {
            id: 1
            name: "qwe"
            age: 8.5
        },
        {
            id: 2
            title: "asd"
        }
    ]



    // blob is base64 encoded array of bytes
    blob: blob"""
    TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0
aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1
c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0
aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdl
LCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4="""
}
