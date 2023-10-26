Release history
===============

.. currentmodule:: outcome

.. towncrier release notes start

Outcome 1.3.0 (2023-10-17)
--------------------------

Features
~~~~~~~~

- Added type hints to the package. :py:class:`Value` and :py:class:`Outcome` are now generic.
  A type alias was also added (:py:data:`Maybe`) for the union of :py:class:`Value`
  and :py:class:`Error`. (`#36 <https://github.com/python-trio/outcome/issues/36>`__)


Outcome 1.2.0 (2022-06-14)
--------------------------

Features
~~~~~~~~

- Add support for Python 3.9 and 3.10. (`#32 <https://github.com/python-trio/outcome/pull/32>`__)


Deprecations and Removals
~~~~~~~~~~~~~~~~~~~~~~~~~

- Drop support for Python 3.6. (`#32 <https://github.com/python-trio/outcome/pull/32>`__)


Outcome 1.1.0 (2020-11-16)
--------------------------

Bugfixes
~~~~~~~~

- Tweaked the implementation of ``Error.unwrap`` to avoid creating a
  reference cycle between the exception object and the ``unwrap``
  method's frame. This shouldn't affect most users, but it slightly
  reduces the amount of work that CPython's cycle collector has to do,
  and may reduce GC pauses in some cases. (`#29 <https://github.com/python-trio/outcome/issues/29>`__)


Deprecations and Removals
~~~~~~~~~~~~~~~~~~~~~~~~~

- Drop support for Python 2.7, 3.4, and 3.5. (`#27 <https://github.com/python-trio/outcome/issues/27>`__)


Outcome 1.0.1 (2019-10-16)
--------------------------

Upgrade to attrs 19.2.0.


Outcome 1.0.0 (2018-09-12)
--------------------------

Features
~~~~~~~~

- On Python 3, the exception frame generated within :func:`capture` and
  :func:`acapture` has been removed from the traceback.
  (`#21 <https://github.com/python-trio/outcome/issues/21>`__)
- Outcome is now tested using asyncio instead of trio, which outcome is a
  dependency of. This makes it easier for third parties to package up Outcome.
  (`#13 <https://github.com/python-trio/outcome/issues/13>`__)


Outcome 0.1.0 (2018-07-10)
--------------------------

Features
~~~~~~~~

- An Outcome may only be unwrapped or sent once.

  Attempting to do so a second time will raise an :class:`AlreadyUsedError`.
  (`#7 <https://github.com/python-trio/outcome/issues/7>`__)
