# Contributing

Thanks for thinking about contributing to the development of Pyourls3 - it means a lot. Following the guidelines set out
below means you're more likely to receive positive feedback from the developers and project maintainers. 

## **Wanted contributions**

Examples of good contributions are as follows:

* Updates to documentation
* Submitting bug reports and fixing minor bugs
* Feature requests
* Writing code that could be incorporated into Pyourls3 itself
* Using the issues section for questions is ok, provided that the question label is applied.

## **Unwanted contributions**

Please don't make large changes without prior consultation - these are likely to be closed and ignored. Transparency is
key.

## **Expectations**

* Be welcoming to newcomers
* Create issues for major changes and enhancements
* Please try to avoid creating new classes - instead try to use new functions
* Ensure that a suitable range of tests are carried out

## **Your first time?**

Everyone was a beginner once. This entire package was created as a learning experience. If you're working on a pull request,
check out this free series, [[how to contribute to an open source project on Github]](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github).

## **How to submit**

The general procedure for any change, regardless of it's size is as follows:

* Create your own fork of the repository
* Make your changes in your fork
* Submit a pull request

## **Filing bug reports**

There is a bug report template already setup within the GitHub repository, but it will also be included here:
    
    **Platform info (please complete the following information):**
     - OS: [e.g. iOS]
     - Python Version: [e.g. 3.7.4, 3.5.3, etc]
     - Package version: (found in `pyourls3.version`)
    
    **Describe the bug**
    A clear and concise description of what the bug is.
    
    **To Reproduce**
    Steps to reproduce the behavior:
    1. Go to '...'
    2. Click on '....'
    3. Scroll down to '....'
    4. See error
    
    **Expected behavior**
    A clear and concise description of what you expected to happen.
    
    **Additional context**
    Add any other context about the problem here.
    
Please also label your bug report with the "bug" label.

## **Review process**

For any pull requests that are submitted, the maintainers and developers have the final say. They will decide if the pull
request is worthy of being incorporated into the main project, and if not, may specify a reason why.

## **Code style**

Code styling is simple: follow [[PEP-8]](https://www.python.org/dev/peps/pep-0008/) and try to start boolean variable names
with `is` or `should`, or something along the lines of that.

    self.is_using_signature_auth = False