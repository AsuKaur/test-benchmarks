#include "verifier_functions.h"

int main()
{
	float a, b;

	a = __VERIFIER_nondet_float();
	b = __VERIFIER_nondet_float();

	__VERIFIER_assume(a >= 0.0f && a <= 1.0f);
	__VERIFIER_assume(b >= 0.0f && b <= 1.0f);

    float sum = a + b;

    __VERIFIER_assert(sum <= 2.0f);

	return 0;
}