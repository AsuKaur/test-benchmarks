#include "verifier_functions.h"

int main()
{
	float a, b;

	a = __VERIFIER_nondet_float();
	b = __VERIFIER_nondet_float();
	
	// a >= 0.0 & a <= 1.0
	__VERIFIER_assume(a >= 0.0f && a <= 1.0f);
	//  b >= 0.0 & b <= 1.0
	__VERIFIER_assume(b >= 0.0f && b <= 1.0f);

    float mul = a * b;

	// UNSAFE: mul > 1.0
    __VERIFIER_assert(mul > 1.0f);

	return 0;
}