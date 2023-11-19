# TutoringWebsite

**A practice website built with Django for a fictional tutoring business - ACE Tutoring**

*Link to Kanban board for project: [ACE Tutoring Kanban Board](https://github.com/users/smithoj1171077/projects/3/views/1)*

**Owner:** Oliver Smith  
**Stakeholders:** ACE Tutoring owner, tutors, and customers  
**Status:** In planning  
**Release target:** 19th November  
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
- Product owner accepts it.

### Tutor Browsing

As a customer, I want to search for a tutor in a particular subject and review their background, availability, and session details.

**Acceptance Criteria:**
- Browse page with tutor profiles.
- Filters for subject, availability, session type, and location.
- Session location filter requires user's suburb.
- Integrated with the view tutor page.

**Definition of Done:**
- Implemented and works correctly.
- User-friendly.
- Search has useful and reasonable filters.
- Integrated with the view tutor page.

### Tutor Details

As a customer, I want to send a request for a tutor based on specific criteria.

**Acceptance Criteria:**
- Tutor view page with photo, background, and availability.
- Request booking button leading to the request booking page.

**Definition of Done:**
- Information displayed nicely with no bugs.
- Integrated with the site.

### Booking Page

As a customer, I want to send a tutoring request with minimal form-filling.

**Acceptance Criteria:**
- Form linked from tutor details or main page.
- Mandatory fields: subject, student name, purchaser name, contact number.
- Optional fields: time availabilities, preferred locations, and preferred tutor.
- Database stores the form.
- Business manager account is notified.

**Definition of Done:**
- Fully functional and passes testing.
- Product owner finds it acceptable.

### Review Request Page

As the business manager, I want a private dashboard to review the latest request forms.

**Acceptance Criteria:**
- Scroll-down list of new requests ordered by the latest.
- Details of requests displayed.
- Owner can mark as resolved and remove them from the queue.

**Definition of Done:**
- Implemented and working.
- Properly integrated into the website.

## About Us

[Content about the business]

## Buy

[Information about purchasing materials]
