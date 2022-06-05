# Stack
 + Grows towards 0
 + Think of stack frame as a function in C
   - EBP points to the bottom of stack
    * address of `ret` will be `EBP+4`
   - ESP points to the top of the stack

 + Example C:                  fucn's stack frame
 ```                           ```
 void func(int x) {             | ...                  | << ESP
     int a = 0;                 ------------------------
     int b = x;        Reg >>   | 10 (passed argument) |
                        10      ------------------------
 }                       ^      | 0 (value of a)       | << EBP
 int main() {            |      ------------------------
     func(10);           |      | ret addr to main     | << EBP+4
                         |      ------------------------
 }                       |__    | 10 (the argument)    |
                                ------------------------
 ```                           ```

