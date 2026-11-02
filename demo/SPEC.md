# shipping_cost(weight_lb) – requirement

Returns the shipping price in dollars for a package of `weight_lb` pounds.

- Weight of zero or less: raise `ValueError`.
- More than 0 lb, up to and including 1 lb: $5.00
- More than 1 lb, up to and including 5 lb: $9.00
- More than 5 lb: $9.00 plus $2.00 for each started pound over 5.
  - 5.1 lb → $11.00
  - 6 lb → $11.00
  - 6.5 lb → $13.00
