# TutoringWebsite

**A practice website built with Django for a fictional tutoring business - ACE Tutoring**

*Link to Kanban board for project: [ACE Tutoring Kanban Board](https://github.com/users/smithoj1171077/projects/3/views/1)*

**Owner:** Oliver Smith  
**Stakeholders:** ACE Tutoring owner, tutors, and customers  
**Status:** In planning    
**All responsibilities are on Oliver Smith**

## Background

ACE Tutoring specializes in helping high school students with their final year exams and assessments. The business employs tutors who provide one-on-one help to students and creates/sells materials like subject guides and revision sheets.

## Strategic Fit

Currently relying on word of mouth, ACE Tutoring aims to expand its customer base through a website and social media advertising. The website aims to enhance customer convenience in arranging tutoring and purchasing materials.

## Goals

Create a website to increase business reach, featuring an appealing layout. Provide a convenient portal for customers to arrange tutoring services and purchase material. Include facilities for customers to review services, send requests for tutors, and purchase materials.

## User Stories

### Blog Posts

As the ACE Tutoring business owner, I want to upload blogs about subjects to my site for prospective customers.

**Acceptance Criteria:**
- A panel linking to the blog posts on the main page.
- Each post includes title, author, date, tags (subject), and an optional image.
- Latest blog post appears at the top.
- Customers can filter by subject.
- Link takes the user to a page with full blog information.

**Definition of Done:**
- Implemented and passes testing.
- Aesthetically pleasing and easy to use.
- All stakeholers accept it.
<br>
![](https://github.com/smithoj1171077/TutoringWebsite/blob/b39e39c3890139a276e14f3ff4fdfbc655d5a3e4/Exploring_blogs.gif)

### Booking Page

As a customer, I want send the required information to get tutoring services online because that allows me to do it where ever and whenever I please as opposed to having to ring the business

**Acceptance Criteria:**
- Form linked from  main page.
- subject (at least one, at most four), student name, parent or guardian name, at least one of contact number, student email or parent/guardian email.
- online only, and postcode (online only is for if the student is distance learning; if it is ticked false then the assumption is that the student wants inperson sessions at their house).
- if not online only then the postcode entered must be a valid Australian postcode and must be within 30 kms of the tutoring business postcode. 
- Database stores the form.
- Business manager account is notified.

**Definition of Done:**
- Fully functional and passes testing.
- Product owner finds it acceptable.



## Store

As a student/parent I want to be able to purchase additional subject guides from the tutoring business. 

**Acceptance Criteria:**
- front page links to index where the user can view the items for sale
- user should be able to filter by subject
- user should be able to click on an item and see a description, photo and price
- add to cart
- check out form
- database storage of items

**Definition of done**
- Fully functional and passes testing
- is asethetically appealing and easy to use 

