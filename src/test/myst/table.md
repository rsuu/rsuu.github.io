## table

### markdown table

:::{table} 1
:align: center
:widths: grid

abc | mnp | xyz
--- | --- | ---
123 | 456 | 789
:::

| a | b |
|:-|:-|
1|2
3|4


### rst table

:::{eval-rst}
:align: center
:widths: grid

+----+------+------------+
| s  | awd  |    aaaaa   |
+====+======+============+
| s  | awd  |  ss        |
| a  |      |       ss   |
| s  | awd  |  cc        |
+----+------+------------+


+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+



+----------------------------------------------------------+------------------------------------------------------+
| ::                                                       |                                                      |
|                                                          |                                                      |
|    -a            command-line option "a"                 |    -a            command-line option "a"             |
|    -b file       options can have arguments              |    -b file       options can have arguments          |
|                  and long descriptions                   |                  and long descriptions               |
|    --long        options can be long also                |    --long        options can be long also            |
|    --input=file  long options can also have              |    --input=file  long options can also have          |
|                  arguments                               |                  arguments                           |
|    /V            DOS/VMS-style options too               |    /V            DOS/VMS-style options too           |
+----------------------------------------------------------+------------------------------------------------------+

:::


### csv table

:::{csv-table}
:header: "Treat", "Quantity", "Description"
:widths: 15, 10, 30

"Albatross", 2.99, "On a stick!"
"Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
crunchy, now would it?"
"Gannet Ripple", 1.99, "On a stick!"

:::