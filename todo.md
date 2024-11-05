need to figure out how to condense the manpages down to make the speed more practical if we're doing
it locally

getting it to output shorter things also a good idea

think about doing this on arch so we can rollback changes... modifying conf files.. something like
that.

non-chaos mode: make it a separate user without a lot of access

evaluate: concrete tasks of find that it should perform
.. maybe some kind capture the flag in the os

input text - what the corresponding output should be
- can either be the raw command that should get run
- or more broadly what it should be
    - needs to be clear how we know it succeeded, the path to the file
    - how many files are in this folder / answer
    - would need to make a repo that includes the standard environment where the commands should be
        run so that the correct answers make sense

you can define some of the tests afterwards, but start with some that you want it to be able to do
like, do two or three test cases for find
