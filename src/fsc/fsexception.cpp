#include <stdio.h>
#include <stdlib.h>
#include "stdfsc.h"
#include "fstype.h"
#include "fsexception.h"

void FSThrowMemoryException()
{
	throw CFSMemoryException();
    //fprintf(stderr, "CFSMemoryException!\n");
    //fflush(stderr);
    //exit(1)
}
