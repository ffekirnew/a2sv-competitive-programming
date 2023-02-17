/**
 * @param {string[]} source
 * @return {string[]}
 */
var removeComments = function removeComments(source) {
  // object to be returned
  let out_put = [];

  // create a flag to know if in comment
  let in_comment = false;

  // iterate the source code
  for (let line of source) {
    if (!in_comment) {
      out_put.push([]);
    }
    let i = 0;
    while (i < line.length) {
      let char = line.charAt(i);
      if (in_comment) {
        if (char === '*' && i + 1 < line.length && line.charAt(i + 1) === '/') {
          in_comment = false;
          i += 1;
        }
        i += 1;
      } else {
        if (char === '/' && i + 1 < line.length && line.charAt(i + 1) === '*') {
          in_comment = true;
          i += 1;
        } else if (char === '/' && i + 1 < line.length && line.charAt(i + 1) === '/') {
          break;
        } else {
          out_put[out_put.length - 1].push(char);
        }
        i += 1;
      }
    }
    if (!in_comment) {
      let new_line = out_put.pop().join('');
      if (new_line) {
        out_put.push(new_line);
      }
    }
  }
  return out_put;
}