# PROGRAM ARCHIVE

### "hello"

```
!5
8333318318.3.4418.3.4418.3.36
```

(packets: "plus100.123")
```
.3333333333.
```

no addons

--_-_-_-_-_-_-_-_-

### raw "hello"

```
!5
.3333333333.33331
.3333333333.31
.33333333333.441
.33333333333.441
.33333333333.36
```

no packets, no addons

--_-_-_-_-_-_-_-_-

### add-on test

```
!1
/6
```

no packets

```python
9 addons 9
def test():
    s = sys.modules["__main__"]
    s.mem[s.cur] += 101

9 "/": test 9
```

--_-_-_-_-_-_-_-_-

### the adder

```
!2

>1>2.+.9.5.
```

no packets

general.py addons

--_-_-_-_-_-_-_-_-

### get request

```
h33331
.h3.44441
.h3.44441
.h.331
.h.333331
.333333.441
.33333.4441
.33333.4441
h33331
.h3.44441
.h3.44441
.h.331
h441
h333331
.h.1
.33333.44441
.h.31
.h.33331
h3331
.33333.4441
h3331
h31
.h3.44441
6
._.
```

no packets
general.py

--_-_-_-_-_-_-_-_-

### guess the number

```
!43

.@.
.3333.333331
.333.331h.444.31h.44.333331h.444.41h.44.3331h.44.3331
.333.331h.44.33331h.444.331h.444.41
.333.331h.44.441h.44.333331h.44.4441h.444.44441h.444.41h.44.331
.333.331.3333.333331
690
.h3.31.h.31.h3.4441
.333.331h3331h31.h3.44441
.333.331.33333.31
.333.331h3331.h3.4441h31.h.333331.h.333331h31.h.333331
.333.331.h3.44441.h.31
.333.331h3331.h3.4441h31.h.333331.h.333331
.333.331h4441
.333.331.33333.41.3333.333331h1h333331h3331h333331.h3.44441
.333.331.h.1.h3.4441.h.41h441h31.h.33331
690

~ main loop ~
.h.1.h3.4441.h.41h441h31.h.33331.333.331.33333.4
6908
.h.1.h3.4441.h.41h441h31.h.33331.333.331.33333.
6908
.h.1.h3.4441.h.41h441h31.h.33331.333.331.33333.3
6908
```

packets
```
h33331.h3.44441.h3.44441.h.331.h.333331h.4444.441.33333.4441.33333.4441
h4441.h.331h333331.h.4441h31.h.333331h333331.33333.44441
h3331.h.441h333331.h3.44441h41h33331.33333.44441
.h.41h31.33333.4441
.h.441h3331.h3.44441
.33333.4441
<1
.33333.4441
.:_.90
```

general addons

NOTE: this one usually returns bad request because of glitch.com (it would work if glitch worked), the website URL is created in the packet, if you have an alternative to the following express.js code, please fix my requests

```javascript
const port = process.env.PORT || 3000;

const express = require("express");
const app = express();

app.use(express.static("public"));
app.use(express.urlencoded({ extended: true }));

app.get("/lgt/:num/:secret", (req, res) => { 
  var num = req.params.num; var secret = req.params.secret;
  if(num == secret) {res.send("CORRECT!!! (press ctrl+c to exit)");}
  else if(num > secret) {res.send("guess is greater...");}
  else if(num < secret) {res.send("guess is lesser...");}
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
```

UPDATE: As of 1.0.1, I made APIs for specific programs
ʘ can replace the whole get thing

```
!43

.@.
.3333.333331
.333.331h.444.31h.44.333331h.444.41h.44.3331h.44.3331
.333.331h.44.33331h.444.331h.444.41
.333.331h.44.441h.44.333331h.44.4441h.444.44441h.444.41h.44.331
.333.331.3333.333331
690
.h3.31.h.31.h3.4441
.333.331h3331h31.h3.44441
.333.331.33333.31
.333.331h3331.h3.4441h31.h.333331.h.333331h31.h.333331
.333.331.h3.44441.h.31
.333.331h3331.h3.4441h31.h.333331.h.333331
.333.331h4441
.333.331.33333.41.3333.333331h1h333331h3331h333331.h3.44441
.333.331.h.1.h3.4441.h.41h441h31.h.33331
690

~ main loop ~
.h.1.h3.4441.h.41h441h31.h.33331.333.331.33333.4
690<ʘ9
.h.1.h3.4441.h.41h441h31.h.33331.333.331.33333.
690<ʘ9
.h.1.h3.4441.h.41h441h31.h.33331.333.331.33333.3
690<ʘ9
```

--_-_-_-_-_-_-_-_-

### Hello, \[Name\]!

```
!100

h.4.4441h33331h4441.h3.44441.3333.41.h3.444441.333.331.h3.31.h.31.h3.4441.h.33331.333.331.h.1h4441.h.41h31h.4444.33369
h.444.331h31.h.441.h.441.h.31.3333.33331.333.331=1.333.33316
```

no packets
general addons

--_-_-_-_-_-_-_-_-

### Cat Program

```
!100
09=6i
```

no packets
general again

--_-_-_-_-_-_-_-_-

### a walk down the ASCII catalog

```
356.=.i
```

general.py

--_-_-_-_-_-_-_-_-