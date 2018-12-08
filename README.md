# mrpackerjs
Javascript mrpacker library - faster and smaller than JSON

# Usage

Include it with

```html
<script src="https://cdn.jsdelivr.net/gh/MarkReedZ/mrpackerjs/mrpacker.min.js"></script>
```

And test with

```javascript
  var o = [1,2,3,100,2000];
  console.log( mrpacker.unpack( mrpacker.pack(o) ));
```
