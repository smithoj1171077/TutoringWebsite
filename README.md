# TutoringWebsite
A practice website build with Django for a fictional tutoring business
ACE Tutoring website

link to Kanban board for project: https://github.com/users/smithoj1171077/projects/3/views/1
 
Owner: Oliver Smith
Stakeholders: ACE Tutoring owner, tutors, and customers
Status: in planning
Release target 19th November
All responsibilities are on Oliver Smith
 
background
 
ACE Tutoring specializes in helping high school students with their final year exams and assessments; the business employs tutors who provide one-on-one help to students. They also create and sell material such as subject guides and revision sheets to students.
 
Strategic fit
 
Currently, ACE Tutoring's primary source of customers is word of mouth and is thus limited to a smaller market. The website combined with advertising on social media is intended to expand the base of customers. Furthermore, the convenience of being able to arrange tutoring or purchase revision books online should boost demand for ACE Tutoring services.
 
Goals
 
Create a website that increases the reach of the business with a layout and provides a convenient portal for customers to arrange tutoring services and purchase material. There should be an appealing front page that entices the customers on entering the website, facilities for customers to review tuition services for different subjects send a request to the business to organize a tutor. There should be facilities to purchase the material created by the website.
 
User stories
 
---------------------------------------------------------
 
Blog posts:
 
As the ACETutoring business owner, I want to be able to upload blogs about subjects to my site for prospective customers, who may find them insightful and thus more ready to make a purchase or return to the website to read more.
 
Acceptance Criteria
 
There should be a panel linking to the blog posts on the main page
Each post should include the title, author, date, and some tags such as the subject and an image if one has been provided
By default, the top of the list should be the latest blog post
Customers should be able to filter by subject
The link should take the user to a page that as all the basic information outlined in (2.) plus also the full blog
Definition of done:
The feature is implemented and passes testing
It is asethtically pleasing and easy to use for uploaders and end users 
The product owner accepts it
-------------------------------------------
Tutor browsing 
As a customer I want to be able to search for a tutor in a particular subject, to be able to review their background, i.e academic record and availability and to know if they  do online or inperson appointments. Also I want to know where they are able to meet for sessions. 
Acceptance criteria 
A browse page which contains the profiles of tutors employed by the company
The user should be able to filter the list with drop down buttons for subject, availability, session type, and session location.
The session location filter first needs the customer to enter the suburb they want the session to take place in; all tutors who are 'out of range' are filtered out.
Definition of done 
Feature is implemented and works correctly
is shown to be easily usable 
The search Has all the filters which are useful to the customer and reasonable to implement 
The search page is integrated with the view tutor page 
-------------------------------------------- 
Tutor details

As a customer I want to be able to send a request to the business for a tutor, either with a specific tutor I searched for, or a request based on the specific criteria I have filled out for the business owner to then find someone who fits it 

Acceptence criteria 
The tutor view page contains all the information about the tutor including a photo, their background, i.e academic record and availability and to know if they do online or inperson appointments. 
There is a request booking button which takes the user to the request booking page
Definition of done
all the information is displayed nicely and there are no bugs
the page is integrated with the rest of the site 
-------------------------------------------
Booking page

As a customer I want to send a request in to the business for tutoring. I want to spend only the minimum necessary amount of time filling out forms. Therefore any information I have already provided in the filters should be auto-filled in the form if applicable. The form should include: the subject (mandatory), student name, purchaser name, contact number, time availabilities, preferred locations and preferred tutor. 

Acceptence criteria 
The form is linked to from either the tutor details page or the main page 
The following fields are present: mandatory: subject, student name, purchaser name, contact number. Optional: time availabilities, preferred locations and preferred tutor. 
The database stores the form
The business manager account is notified 
Definition of Done:
The feature is fully functional and has passed testing 
the product owner finds it acceptable
--------------------------------------------
Review request page
As the manager of the business, I want a private dashboard to review the latest request forms submitted by customers. I want to see only the requests I have not responded to yet so my inbox is not cluttered. 

Acceptance criteria 
There is a scrolldown list of new requests ordered by latest
The details of the requests are displayed
The owner can mark as resolved and remove them from the que
Definition of done
The feature is implemented and working
it is properly integrated into the rest of the website 
----------------------------------------
About us 
---------------------------------------
Buy
