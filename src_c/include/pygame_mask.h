/*
  pygame-ce - Python Game Library

  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Library General Public
  License as published by the Free Software Foundation; either
  version 2 of the License, or (at your option) any later version.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Library General Public License for more details.

  You should have received a copy of the GNU Library General Public
  License along with this library; if not, write to the Free
  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
*/

#ifndef PGMASK_H
#define PGMASK_H

#include <Python.h>
#include "bitmask.h"

typedef struct {
    PyObject_HEAD bitmask_t *mask;
    void *bufdata;
} pgMaskObject;

#define pgMask_AsBitmap(x) (((pgMaskObject *)x)->mask)

#endif /* ~PGMASK_H */
