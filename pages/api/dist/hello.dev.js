"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
var _default = function _default(req, res) {
  res.statusCode = 200;
  res.json({
    name: 'John Doe'
  });
};

exports["default"] = _default;