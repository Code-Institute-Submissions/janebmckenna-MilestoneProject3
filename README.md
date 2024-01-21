# Life in Blog
[View live project Here](https://life-in-blog-cd65fb4d61a0.herokuapp.com/)
***

Life in Blog is a user centric app designed to enable users to follow and extract inspiration from others life experiences. Users can blog their life experiences, be it travel, food, books, film or day to day life. A tough life experience blog for others may help to avoid a pitfall in the road. Life in Blog allows users to write about all of lifes experiences, ups and downs.  

![Mock Up](static/Images/mockup.png)

- [Blog Website](#blog-website)
- [User Experience UX](#user-experience-ux)
  - [UX-strategy](#ux-strategy)
  - [UX-scope](#ux-scope)
  - [UX-structure](#ux-structure)
  - [UX-skeleton](#ux-skeleton)
  - [UX-surface](#ux-surface)
- [Technologies-used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

# User Experience UX

## UX-strategy

The goal is to provide a blog website for users to post their thoughts and feelings on various subjects from books, tv shows to day to day life. 

**Developer Goals**
- Build portfoilio: 
- Develop technical skills:

The MVP of this project is simple but the app can be developed to include commenting on other posts, celebrating the post content, including images and potential monitisation through advertising or affliate links. 



**User Goals**
- Access to imformation and inspiration, what book will they read next or where will they travel to?
- Passing time reading content.
- Seemless Navigation
- Sharing content/Post their thoughts and feelings on a variety of subjects. 
- Search blogs for a specific user or content. 
- Responsive design. Can be accessed on the go. 


**User Stories**

_As a FIRST TIME user of the site I want to be able to:_
- Intuitively and easily navigate the site
- Browse blog content
- Register as a user
- Logout of the site

_As a RETURNING user of the site I want to be able to:_
- Login and out of the site.
- Easily filter to my favourite blogger
- Write my own blogs
- Edit/Update my blogs
- Delete my blogs
- Comment on other users blogs

_As an admin of the site I want to be able to:_
- Edit or Delete all Blogs
- Manage the blog categories
- Delete all comments


## UX-scope

**Existing Features**

**Home Page**

![homepage LoggedOut](static/Images/homepage(loggedout).png)

**Nav Bar**

Links available within the navbar vary dependent on access. 

_Logged Out_

![Nav LoggedOut](static/Images/Nav(loggedout).png)

_Logged In_

![Nav LoggedIn](static/Images/nav(loggedin).png)

_Admin_

![Nav Admin](static/Images/nav(admin).png)

**Logo**

![Logo](static/Images/logo-white.png)

**Search Feature**
Search allows users to search by username, category, or keywords from the title and/or content of the blog. 

![Search](static/Images/search.png)

**Blog Feed**
Blog feed displays the most recent by date created at the top of the feed. In future I could expand this to log the time and date the post is created to curate the display further. 

![blog feed](static/Images/blogs.png)

**Footer**

**Register Page**

![registration form](static/Images/register.png)

**Login Page**

![Login](static/Images/Login.png)

**Profile Page**

**Logout**

![Logout](static/Images/logout.png)

**Administrator Features**
- Manage Categories
- Delete Blogs
- Delete Comments

**Commenting on blogs**

I decided to avail of the flexibility of a non relational database by simply storing comments in an array within the blog object. To maintain visability of which user commented without relating directly back to the user object within the database I pushed the username to the database as part of the comment. 

**CRUD Functionality**

User recieves feedback when actions are complete and is asked to confirm before deletion. 

![User Feedback](static/Images/blog(add).png)

_Create:_ 
I can create user account, blog posts and comments. 

![Register Account](static/Images/register.png)

_Read:_ 
I can read all user blogs and comments

![Read blog and comments](static/Images/readcomments.png)

_Update:_
I can update my own blogs

![Edit Blog](static/Images/edit.png)

_Delete:_
I can delete my own blogs. 

![Delete Blog](static/Images/deleteblog.jpg)

Additionally as an admin I can also:
CRUD - categories, all blogs and all comments. 

**Future Improvements**
- Contact page
- Ability to celebrate Blogs
- Reset password function

**Celebrating blogs**

  
## UX-structure

**Navigation**
I have decoded to use a traditional navigation bar with links displaying to the relevant users.
Not logged in users will see - Home, Login and Register
Logged in users will see - Home, Logout, New Blog, Profile
Admin users will see - Home, Logout, New Blog, Profile and manage categories. 

The Navigation bar collapses into a hamburger icon which users are familiar with on mobile devices. 


**Footer**



**Data Structure**
![Data Structure](static/Images/Wireframes/Database.png)


## UX-skeleton

**Design Choices**



**Wireframes**

[View Wireframes](wireframes.md)

## UX-surface

**Colour Palette**


**Fonts**



**Responsiveness**
I will rely upon a combination of materialize and media queries to ensure the app was was visually appealing and well laid out on all screens. 


# Technologies-used
- **Libraries:** jQuery, Materialize, Flask
- **Languages:** HTML, CSS, JavaScript, Python
- **Database Management:** MongoDB
- **Gitpod:** used as a cloud code editor.
- **GitHub:** used as a cloud based code repository.
- **Heroku:** was used to deploy the app. 

# Testing 
[View Testing Documentation](testing.md)

# Deployment
The Website has been deployed using Heroku [Here](https://life-in-blog-cd65fb4d61a0.herokuapp.com/) using the method below:

- I logged into my Heroku Account. 
- I clicked on New and choose 'Create New App'
- I choose a unique name for my app and set the region to Europe. 
- I then chose Github as the deployment method and searched for my repo name. 
- I then clicked on settings and  updated the config variables. 
- I navigated back to the deploy and enabled automatic deployment. 


# Credits
**Content**

- [Materialise Version 1.0.0](https://materializecss.com/about.html)
- I used [mycolor.space](https://mycolor.space/) to decide on the colour scheme of the site.
- Icons were sourced from [Font Awesome](https://fontawesome.com)
- My fonts were taken from [Google Fonts](https://fonts.google.com/)
- Wireframes were created using [Balsamiq](https://balsamiq.com/)
- I used [Lucid Chart](https://www.lucidchart.com) 

**Code**
- I learned how to format the date within my Python function from [this site ](https://stackoverflow.com/questions/62762873/current-date-time-in-a-particular-format-python) 
- I learned how to delete an object from an array in MongoDB in the documentation [here](https://www.mongodb.com/docs/manual/reference/operator/update/pull/#:~:text=If%20the%20specified%20to,exact%20same%20fields%20and%20values.)
- While developing this project I refered back to code I had written during the task manager mini project.



**Advice**


