# Vueify

A Python3/Binary script to convert `.html`, and `.css` structure into `.vue` structure recursively in a directory.

## Table of Contents

- [Vueify](#vueify)
  - [Table of Contents](#table-of-contents)
  - [Compilation](#compilation)
  - [Usage](#usage)
    - [Bootstrap Studio](#bootstrap-studio)
    - [Standalone (Python3)](#standalone-python3)
    - [Standalone (Binary)](#standalone-binary)
  - [Example](#example)

## Compilation

1. Make sure you have Python3, Nuitka, and a compatiable C compiler installed.
2. Run the `build.sh` script with the path of the python source code as the only argument: `./build.sh vueify.py`.
3. This will create a `./dist` directory containing the `vueify` binary and resource files.

## Usage

### Bootstrap Studio

1. Open Bootstrap Studio.
2. Open the **Export Settings** dialogue.
3. Expand the **Advanced** area.
4. Browse and select the `vueify` binary.
5. Run your export as normal.

### Standalone (Python3)

1. Open a terminal.
2. Navigate to the directory containing `vueify.py`.
3. Execute the following: `python vueify.py directory_containing_html_files`.

### Standalone (Binary)

1. Open a terminal.
2. Navigate to the directory containing `vueify` binary.
3. Execute the following: `./vueify directory_containing_html_files`.

## Example

If the `.vue` does not exist, it will create a new one, else it will only replace the `<template></template>` contents. Not all files will work – if there are unknown encodings, vueify will fail.

`example.html`:

```html
<html>
  <head>
    <title>An example</title>
    <meta charset="utf-8">
  </head>
  <body>
    <div>
      <p>Hello World!</p>
    </div>
  </body>
</html>
```

`./assets/css/example.css`

```css
.a {
  color: red;
}

.b > .a {
  color: blue;
}
```

`example.vue`:

```html
<!-- HTML -->
<template>
  <div>
    <p>Hello World!</p>
  </div>
</template>
<!-- JS -->
<script>
export default {}
</script>
<!-- CSS -->
<style scoped="">
.a {
  color: red;
}

.b > .a {
  color: blue;
}
</style>
```
