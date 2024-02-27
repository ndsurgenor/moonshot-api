# moonshot-api : Backend Testing

_Note: to open links in a new tab, hold CTRL + Click_<br>
_Note: this document only contains testing info for the moonshot frontend site_
- _If you require testing info for the frontend please [click here to access moonshot/TESTING.md](https://github.com/ndsurgenor/moonshot/blob/main/TESTING.md)_
- _If you require full documentation please [click here to access the README.md](README.md) file_

## Table Of Contents
- [Introduction](#moonshot-api--backend-testing)
- [Manual Testing](#manual-testing)
    - [User Administration](#user-administration)
    - [GPPD (CRUD) Functionality](#get-post-put--delete-crud-functionality)
        - [User & Equipment Profile Tests](#user--equipment-profile-tests)
        - [Photo Tests](#photo-tests)
        - [Comment Tests](#comment-tests)
        - [Star Tests](#star-tests)
- [PEP8 Validator Testing](#pep8-validator-testing)
- [Bugs](#bugs)

## Manual Testing

The following sections list a number of manual tests undertaken to ensure the site operates according to details listed under [Scope](README.md#scope) and [Structure](README.md#structure) in the README file. Specific dev goals/user stories can viewed (where appropriate) by hovering over the numbers listed under 'Ref(s)' in the tables below; clicking these links will open the relevant section in the README file.

### User Administration

These tests check the sign up, sign in, and sign out functionality of the site. The superuser *ms_superadmin* and its related password (not given here for security of the API) along with the general user of username: _testname_, password: _test#123_ have specifically been created to access and function within the backend in order to determine the outcome of these tests. Within the tables below, the descriptor 'valid details' indicates that the following is expected:

- Required fields (*) are not left blank
- Invalid values/formats have not been added to a field

**Test**|**Ref(s)**|**Steps**|**Expected**|**Result**
-----|:-----:|-----|-----|:-----:
Admin can sign into the admin site|[1.1](README.md#milestone-1---api--admin-functionality "Set up Django REST and its supporting libraries via the IDE in order for API development to begin")|<ol><li>Type https://moonshot-api-ff76437bf02f.herokuapp.com/admin/ into the browser</li><li>Enter valid admin details</li><li>Click 'Log in' button</li></ol>|<ul><li>Admin directed to main site administration page</li></ul>|Pass
Admin can add a user, and their related user and equipment profiles, to the site|[1.2](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to create and edit User Profiles so I can control user permissions on the frontend")<br>[1.3](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to review and edit Equipment Profiles for users so I can details on the frontend")|<ol><li>Login in to admin site</li><li>Click 'Add' beside 'Users'</li><li>Scroll to bottom of page and complete form with valid details</li><li>Click 'Save' button</li></ol>|<ul><li>Admin directed to new page displaying name of newly created user</li><li>Newly created user also displayed on 'User profiles' page (click 'User profiles' link to view)</li><li>Newly created user also displayed on 'Equipment profiles' page (click 'Equipment profiles' link to view)</li></ul>|Pass
Admin cannot add a user who already exists|[1.2](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to create and edit User Profiles so I can control user permissions on the frontend")<br>[1.3](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to review and edit Equipment Profiles for users so I can details on the frontend")|<ol><li>Login in to admin site</li><li>Click 'Add' beside 'Users'</li><li>Scroll to bottom of page and complete form with the username 'testname'</li><li>Click 'Save' button</li></ol>|<ul><li>A message saying "A user with that username already exists" appears above the form</li></ul>|Pass
Admin can delete a user, and their related user and equipment profiles, on the site|[1.2](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to create and edit User Profiles so I can control user permissions on the frontend")<br>[1.3](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to review and edit Equipment Profiles for users so I can details on the frontend")|<ol><li>Login in to admin site</li><li>Click 'Users' link</li><li>Scroll down and select tick box beside user to be deleted</li><li>Select 'Delete selected users' from Action dropdown above the user list</li><li>Click 'Go' button</li><li>Scroll down and click 'Yes I'm sure' button</li></ol>|<ul><li>Admin directed back to list of users</li><li>Deleted user no longer appears on list</li><li>Deleted user also removed from 'User profiles' page (click 'User profiles' link to view)</li><li>Deleted user also removed from 'Equipment profiles' page (click 'Equipment profiles' link to view)</li></ul>|Pass

### Get, Post, Put & Delete (CRUD) Functionality

These tests determine if an admin is able to successfully - or otherwise - create (post), view (get), update (put) and/or delete photos, stars, comments, or gear/account info through the backend admin site. In all test cases, **one must first sign in to the admin site** before completing any of the other steps listed (superuser *ms_superadmin* and its related password - not given here for security of the API - have specifically been registered for this purpose), while the descriptor 'valid details' indicates that the following is expected:

- Required fields (*) are not left blank
- Invalid values/formats have not been added to a field

#### User & Equipment Profile Tests

**Test**|**Ref(s)**|**Steps**|**Expected**|**Result**
-----|:-----:|-----|-----|:-----:
Admin can edit User Profile|[1.2](README.md#milestone-1---api--admin-functionality "As a Site Admin I want to be able to create and edit User Profiles so I can control user permissions on the frontend")|<ol><li>Click 'User Profiles' link</li><li>Click on an entry from the displayed user profiles list</li><li>Scroll down and update form with valid details</li><li>Click 'Save' button</li></ol>|<ul><li>Admin directed back to list of user profiles</li><li>A message saying "The user profile {user profile} was changed successfully" appears above the user profile list</li></ul>|Pass
Admin can update user avatar|[1.2](README.md#milestone-1---api--admin-functionality "As a Site Admin I want to be able to create and edit User Profiles so I can control user permissions on the frontend")|<ol><li>Click 'User Profiles' link</li><li>Click on an entry from the displayed user profiles list</li><li>Scroll down and click 'Choose file' button</li><li>Select a valid image file</li><li>Click 'Save' button</li></ol>|<ul><li>Admin directed back to list of user profiles</li><li>A message saying "The user profile {user profile} was changed successfully" appears above the user profile list</li></ul>|Pass
Admin cannot change avatar to non-image file|[1.2](README.md#milestone-1---api--admin-functionality "As a Site Admin I want to be able to create and edit User Profiles so I can control user permissions on the frontend")|<ol><li>Click 'User Profiles' link</li><li>Click on an entry from the displayed user profiles list</li><li>Scroll down and click 'Choose file' button</li><li>Select a non-image file</li><li>Click 'Save' button</li></ol>|<ul><li>A message saying "Upload a valid image. The file you uploaded was either not an image or a corrupted image" appears on the form</li></ul>|Pass
Admin can edit Equipment profile|[1.3](README.md#milestone-1---api--admin-functionality "As a Site Admin I want to be able to review and edit Equipment Profiles for users so I can details on the frontend")|<ol><li>Click 'Equipment Profiles' link</li><li>Click on an entry from the displayed equipment profiles list</li><li>Scroll down and update form with valid details</li><li>Click 'Save' button</li></ol>|<ul><li>Admin directed back to list of equipment profiles</li><li>A message saying "The equipment profile {equipment profile} was changed successfully" appears above the equipment profile list</li></ul>|Pass

#### Photo Tests

**Test**|**Ref(s)**|**Steps**|**Expected**|**Result**
-----|:-----:|-----|-----|:-----:
Admin can upload photo|[1.4](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to review and edit Photo uploads so I can allow and control images on the frontend")|<ol><li>Click 'Add' beside 'Photos'</li><li>Scroll down and complete all form fields with valid details</li><li>Click 'Choose File' an upload a valid image</li><li>Click 'Save' button</li></ol>|<ul><li>Admin directed back to photo list</li><li>Newly submitted photo appears at top of list</li></ul>|Pass
Admin cannot submit form if non-image file is selected |[1.4](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to review and edit Photo uploads so I can allow and control images on the frontend")|<ol><li>Click 'Add' beside 'Photos'</li><li>Scroll down and complete all form fields with valid details</li><li>Click 'Choose File' an upload a NON-IMAGE FILE</li><li>Click 'Save' button</li></ol>|<ul><li>Form will not submit</li><li>A message saying "Upload a valid image. The file you uploaded was either not an image or a corrupted image" appears below the form</li></ul>|Pass
Admin cannot submit form if Title field is blank |[1.4](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to review and edit Photo uploads so I can allow and control images on the frontend")|<ol><li>Click 'Add' beside 'Photos'</li><li>Scroll down and complete all form fields with valid details but leave 'Title' blank</li><li>Click 'Choose File' an upload a valid image</li><li>Click 'Save' button</li></ol>|<ul><li>Form will not submit</li><li>A message saying "This field is required" appears on the form</li></ul>|Pass
Admin cannot submit form if Main Feature field is left as "(Select an option)" |[1.4](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to review and edit Photo uploads so I can allow and control images on the frontend")|<ol><li>Click 'Add' beside 'Photos'</li><li>Scroll down and complete all form fields with valid details but leave 'Main Feature' unselected</li><li>Click 'Choose File' an upload a valid image</li><li>Click 'Save' button</li></ol>|<ul><li>Form will not submit</li><li>A message saying "This field is required" appears on the form</li></ul>|Pass
Admin cannot submit form if Location field is blank |[1.4](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to review and edit Photo uploads so I can allow and control images on the frontend")|<ol><li>Click 'Add' beside 'Photos'</li><li>Scroll down and complete all form fields with valid details but leave 'Location' blank</li><li>Click 'Choose File' an upload a valid image</li><li>Click 'Save' button</li></ol>|<ul><li>Form will not submit</li><li>A message saying "This field is required" appears on the form</li></ul>|Pass
Admin can submit form if Description field is left blank |[1.4](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to review and edit Photo uploads so I can allow and control images on the frontend")|<ol><li>Click 'Add' beside 'Photos'</li><li>Scroll down and complete all form fields with valid details but leave 'Description' blank</li><li>Click 'Choose File' an upload a valid image</li><li>Click 'Save' button</li></ol>|<ul><li>Admin directed back to photo list</li><li>Newly submitted photo appears at top of list</li></ul>|Pass
Admin can submit form if Lens Used, Camera Used, or Other Equipment Used fields are left blank |[1.4](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to review and edit Photo uploads so I can allow and control images on the frontend")|<ol><li>Click 'Add' beside 'Photos'</li><li>Scroll down and complete all form fields with valid details but leave 'Lens Used', 'Camera Used', and 'Other Equipment Used' blank</li><li>Click 'Choose File' an upload a valid image</li><li>Click 'Save' button</li></ol>|<ul><li>Admin directed back to photo list</li><li>Newly submitted photo appears at top of list</li></ul>|Pass
Admin can update photo with valid details|[1.4](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to review and edit Photo uploads so I can allow and control images on the frontend")|<ol><li>Click 'Photos' link</li><li>Click on an entry from the displayed photo list</li><li>Scroll down and update form with valid details</li><li>Click 'Save' button</li></ol>|<ul><li>Admin directed back to photo list</li><li>A message "The photo {photo name} was changed successfully" appears above the photo list</li></ul>|Pass
Admin cannot update photo with invalid details|[1.4](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to review and edit Photo uploads so I can allow and control images on the frontend")|<ol><li>Click 'Photos' link</li><li>Click on an entry from the displayed photo list</li><li>Scroll down and update form with INVALID DETAILS</li><li>Click 'Save' button</li></ol>|<ul><li>Form will not submit</li><li>A message saying "Please correct the errors below" appears above the form</li></ul>|Pass
Admin can delete photo|[1.4](README.md#milestone-1---api--admin-functionality "as a Site Admin I want to be able to review and edit Photo uploads so I can allow and control images on the frontend")|<ol><li>Click 'Photos' link</li><li>Scroll down and select tick box beside photo to be deleted</li><li>Select 'Delete selected photos' from Action dropdown above the photo list</li><li>Click 'Go' button</li><li>Scroll down and click 'Yes I'm sure' button</li></ol>|<ul><li>Admin directed back to list of photos</li><li>A message saying "Successfully deleted 1 photo" appears above the photo list</li><li>Deleted photo no longer appears on list</li></ul>|Pass

#### Comment Tests

**Test**|**Ref(s)**|**Steps**|**Expected**|**Result**
-----|:-----:|-----|-----|:-----:
Admin can add comment to photo|[1.5](README.md#milestone-1---api--admin-functionality "As a Site Admin I want to be able to review and edit Comments so I can allow and control comments on the frontend")|<ol><li>Click 'Add' beside 'Comments'</li><li>Scroll down and complete all form fields with valid details</li><li>Click 'Save' button</li></ol>|<ul><li>Admin directed back to list of comments</li><li>A message saying "The comment {comment name} was added successfully" appears above the comment list</li><li>Newly submitted comment appears at top of list</li></ul>|Pass
Admin cannot add 'blank comment' to photo|[1.5](README.md#milestone-1---api--admin-functionality "As a Site Admin I want to be able to review and edit Comments so I can allow and control comments on the frontend")|<ol><li>Click 'Add' beside 'Comments'</li><li>Scroll down and complete all form fields but leave 'Content' blank</li><li>Click 'Save' button</li></ol>|<ul><li>Form will not submit</li><li>A message saying "This field is required" appears on the form</li></ul>|Pass
Admin can edit comment|[1.5](README.md#milestone-1---api--admin-functionality "As a Site Admin I want to be able to review and edit Comments so I can allow and control comments on the frontend")|<ol><li>Click 'Comments' link</li><li>Click on an entry from the displayed comment list</li><li>Scroll down and update form with valid details</li><li>Click 'Save' button</li></ol>|<ul><li>Admin directed back to comment list</li><li>A message saying "The comment {comment name} was changed successfully" appears above the comment list</li></ul>|Pass
Admin cannot edit comment to be blank|[1.5](README.md#milestone-1---api--admin-functionality "As a Site Admin I want to be able to review and edit Comments so I can allow and control comments on the frontend")|<ol><li>Click 'Comments' link</li><li>Click on an entry from the displayed comment list</li><li>Scroll down and update form so that 'Content' is blank</li><li>Click 'Save' button</li></ol>|<ul><li>Form will not submit</li><li>A message saying "This field is required" appears on the form</li></ul>|Pass
Admin can delete comment|[1.5](README.md#milestone-1---api--admin-functionality "As a Site Admin I want to be able to review and edit Comments so I can allow and control comments on the frontend")|<ol><li>Click 'Comments' link</li><li>Scroll down and select tick box beside comment to be deleted</li><li>Select 'Delete selected comments' from Action dropdown above the comment list</li><li>Click 'Go' button</li><li>Scroll down and click 'Yes I'm sure' button</li></ol>|<ul><li>Admin directed back to list of comments</li><li>A message saying "Successfully deleted 1 comment" appears above the comment list</li><li>Deleted comment no longer appears on list</li></ul>|Pass

#### Star Tests

**Test**|**Ref(s)**|**Steps**|**Expected**|**Result**
-----|:-----:|-----|-----|:-----:
Admin can add star to photo|[1.6](README.md#milestone-1---api--admin-functionality "As a Site Admin I want to be able to review and edit Star ratings (photo ratings) by users so I can allow and control star ratings on the frontend")|<ol><li>Click 'Add' beside 'Stars'</li><li>Scroll down and select a user and photo</li><li>Click 'Save' button</li></ol>|<ul><li>Admin directed back to list of stars</li><li>A message saying "The star {star name} was added successfully" appears above the star list</li><li>Newly submitted star appears at top of list</li></ul>|Pass
Admin can delete star from photo|[1.6](README.md#milestone-1---api--admin-functionality "As a Site Admin I want to be able to review and edit Star ratings (photo ratings) by users so I can allow and control star ratings on the frontend")|<ol><li>Click 'Stars' link</li><li>Scroll down and select tick box beside star to be deleted</li><li>Select 'Delete selected stars' from Action dropdown above the star list</li><li>Click 'Go' button</li><li>Scroll down and click 'Yes I'm sure' button</li></ul>|<li>Admin directed back to list of stars</li><li>A message saying "Successfully deleted 1 star" appears above the comment list</li><li>Deleted star no longer appears on list</li></ul>|Pass

## PEP8 Validator Testing

All files have been passed through the [Code Institute PEP8 Linter](https://pep8ci.herokuapp.com/). The only warnings given were for the settings.py file which contains a small number of long lines (i.e. greater than 80 characters) under AUTH_PASSWORD_VALIDATORS; as this is code implemented by Django itself at setup, these lines will be left unchanged. 

## Bugs

There are no known bugs in the current deployment of the site. A number of bugs were found, added to the [Kanban workflow](https://github.com/users/ndsurgenor/projects/9), and corrected during development. A brief summary of the backend bugs are provided below:

**Type**|**Issue**|**Detail**|**Solution**|**Result**
-----|-----|-----|-----|:-----:
Data|Database won't migrate|After creating the Stars model and serializer, attempted to run migrations using `python manage.py makemigrations` and `python manage.py migrate`. Terminal displays a `UNIQUE constraint not valid` message.|<ul><li>Delete migrations</li><li>Delete and recode Stars app/model</li><li>Rerun migrations</li></ul>|Fixed
Data|Photos POST function creating IntegrityError|When trying to create upload a photo using the POST function the message `django.db.utils.IntegrityError: NOT NULL constraint failed: photos_photo.user_id` appears|<ul><li>Correct syntax of `def perform_create()` method (incorrectly names as `def create_photo`)</li></ul>|Fixed
Connection|API not accepting data from Frontend|When attempting to sign up a new user via the frontend, an error is logged to the console regarding blocked CORS policy and the React 'white screen' is shown|<ul><li>Added `CLIENT_ORIGIN` and `CLIENT_ORIGIN_DEV` variables to the env.py file</li><li>Added code block to settings.py (see under table)</li></ul>|Fixed
Connection|API not sending `profile_id` and `profile_image` variables|When trying to display a user avatar and receive their id on the frontend, a broken image link is shown in the navbar along with an undefined value in developer tools|<ul><li>Removed underscore from `user_profile` and `equipment_profile`in all serializer files</li></ul>|Fixed
Data|Photo Upload/Edit Form not saving details|Date and Time fields displaying errors within the frontend console with regard to null values|<ul><li>Removed `null="True"` on date and time fields in photos model</li><li>Added relevant defaults to date and time fields</li></ul>|Fixed

``` python
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]
if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
```
