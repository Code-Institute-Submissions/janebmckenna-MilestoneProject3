# Testing

[Return to README](README.md)

## Contents

[Manual Testing](#manual-testing) \
[User Story Validation](#user-story-validation) \
[Lighthouse Audit](#lighthouse-audit) \
[Validator Testing](#validator-testing)\
[Bugs](#bugs)

## Manual Testing

**Device and Browser Testing**

|**Testing** |**iPhone12 safari** |**iPad Pro 9.7" safari**|**MacBook Air Chrome**|**MacBook Air Safari**|**Lenovo MS OS Edge**|**Lenovo MS OS Edge**|**Chrome Developer Tools**|
|-----|-----|-----|-----|-----|-----|-----|-----|
|Responsive|
|Delete/Edit buttons visable to owner user|
|Forms won't submit without appropriate information| Yes | Yes|Yes|Yes|Yes|Yes|Yes|
|User Flash messages appear|Yes|Yes|Yes|Yes|Yes|Yes|Yes|

|**Additional Devices Tested Using Chrome Developer Tools**|**Responsive Observations**
|-----|-----|
|Galaxy S9+|
|Galaxy S20 Ultra|
|Pixel 5|
|iPad Air|
|iPad Mini|
|Surface Pro 7|
|Responsive widths to assess breakpoint issues|

**Manual Testing of User Actions**

|**Feature**     |**Action**     |**Expected Behaviour**     |**Result**     |
|----------------|---------------|---------------------------|---------------|
|Nav Bar|Click Logo|Navigates to home page|Pass|
|Nav Bar|Click Home|Navigates to home page|Pass|
|Nav Bar|Click Register|Navigates to registration page|Pass|
|Nav Bar|Click Login|Navigates to login page|Pass|
|Nav Bar|Click My Profile|Navigates to profile page|Pass|
|Nav Bar|Click Logout|Asks user to confirm logout|Pass|
|Nav Bar|Click New Blog|Navigates to new blog page|Pass|
|Nav Bar|Click Manage categories|Navigates to manage categories page|Pass|
|Nav Bar - Mobile|Click hamburger icon|Expands Navigation on right side of screen|Pass|
|Nav Bar - Mobile|Click Home|Navigates to home page|Pass|
|Nav Bar - Mobile|Click Register|Navigates to registration page|Pass|
|Nav Bar - Mobile|Click Login|Navigates to login page|Pass|
|Nav Bar - Mobile|Click Logout|Asks user to confirm logout|Pass|
|Nav Bar - Mobile|Click New Blog|Navigates to new blog page|Pass|
|Nav Bar - Mobile|Click Manage categories|Navigates to manage categories page|Pass|
|Search Function - Homepage|Type search word press enter|Returns appropriate Blogs or No results found|Pass|
|Search Function - Homepage|Type search word click Submit|Returns appropriate Blogs or No results found|Pass|
|Reset Button - homepage|Click reset button|Clears the search bar and reloads all blogs|Pass|
|Accordian - Homepage |click on blog|expands one blog at a time|Pass|
|Delete Button|Click Delete button|Asks user to confirm deletion|Pass|
|Edit Button|Click Edit Button|redirects user to the edit blog screen which is filled with the current blog content|Pass|
|Footer|Click Github logo|Opens Jane McKennas github in a new window|Pass|



## User Story Validation

## Lighthouse Audit

## Validator Audit

## Bugs

|**Bug**|**Resolution**|
|-----|-----|
|Logo not showing on Profile Page|Forgot to use the jinga templating to reference the img file. Only erroring on the profile page as the page required additional parameters to be passed through|
|Non registered user attempted login - errored|I had refactored my login code to check is the user was 'is_admin' but I hadnt tested it with a non registered user, I had to change the order of the function to allow the flash to the non registered user|
|Confirmation of deletion - modal not displaying and/or error|When attempting to reuse my modal to display confirmation of deletion I encountered an issue with passing through the object_id. I have a temporary workaround using js onclick method while I establish how to pass the object_id though the modal|
|Search on profile page redirecting back to home page|I had reused code for the search and on testing realised I was still directing back to the home page. When I corrected this code I realised that as the length of blogs > 0 if you search for a term that exisits in another users blog no blogs appear but the No results found message doesnt appear|


Remove admin cookie on deployed site - non admin
https://www.techwithtim.net/tutorials/flask/sessions


[Return to README](README.md)