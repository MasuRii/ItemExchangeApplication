# Item Exchange & Marketplace Platform

A community-based platform where users can list items they want to exchange or sell and connect with others to trade goods or purchase items using money. This hybrid system supports both bartering and monetary transactions, providing flexibility and enhancing user engagement.

## Minimum Viable Product (MVP) Features

### **1. User Registration and Profiles**
- **Users can create an account using email and password.** *[Signup Page]*
- **Users can create and edit their profile, including name, location, and profile picture.** *[User Profile Page / Edit Profile Page]*
- **Option to add a brief bio, preferred item categories for exchange, and payment details (e.g., PayPal, credit card).** *[User Profile Page / Settings Page]*
- **Verification of payment methods to ensure secure transactions.** *[User Profile Page / Payment Settings Page]*

### **2. Item Listing**
- **Users can create new item listings with title, description, category, condition, price (optional for sale), and photos (up to 5).** *[New Item Listing Page]*
- **Option to choose between Listing for Sale, Exchange, or Both.** *[New Item Listing Page / Listing Type Selector]*
- **Edit or delete existing listings.** *[My Listings Page / Edit Item Page]*
- **Mark items as available or unavailable.** *[My Listings Page / Item Details Page]*
- **Option to add tags for better searchability.** *[New Item Listing Page / Edit Item Page]*

### **3. Search and Browse**
- **Keyword search functionality for items.** *[Search Bar (accessible on all pages) / Search Results Page]*
- **Category-based browsing.** *[Home Page / Categories Page]*
- **Filter options including item condition, location, price range, listing type (sale/exchange), and date listed.** *[Search Results Page / Filter Panel]*
- **Sort results by relevance, price, date, or user rating.** *[Search Results Page / Sort Options]*

### **4. Exchange and Marketplace Proposal System & Offer Management**
- **Users can send proposals to exchange or purchase listed items.** *[Item Details Page / Send Proposal Page]*
  - **For Sales:** Option to buy immediately or send an offer.
  - **For Exchanges:** Option to propose exchanging items or a combination of items and money.
- **Proposal includes offered item(s), monetary offer (if applicable), and an optional message.** *[Send Proposal Page]*
- **Item owners can accept, reject, or counter proposals.** *[Proposals Management Page / Incoming Offers Page]*
- **Secure payment processing for monetary transactions.** *[Checkout Page / Payment Gateway Integration]*
- **Ability to view active, pending, and completed transactions.** *[Transaction Dashboard / Transaction History Page]*

### **5. Rating and Review System**
- **Users can rate other users on a 5-star scale after completing a transaction (exchange or sale).** *[Rate User Page / Transaction Completion Page]*
- **Option to leave a written review along with the rating.** *[Rate User Page / Review Submission Page]*
- **System calculates and displays average user rating.** *[User Profile Page]*
- **Recent reviews visible on user profiles.** *[User Profile Page]*
- **Functionality to report inappropriate reviews or users.** *[User Profile Page / Report User Page]*

### **6. Payment and Transaction Management**
- **Integrated secure payment gateway (e.g., Gcash, Paymaya) for handling transactions.** *[Payment Gateway Integration]*
- **Refund and dispute resolution mechanisms.** *[Support Page / Dispute Resolution Page]*
- **Transaction history with detailed records of all monetary and barter exchanges.** *[Transaction History Page]*

### **7. Notification System**
- **Push notifications for new proposals, messages, payments, and status updates.** *[System Notifications / Push Notifications Service]*
- **In-app notification center to view all alerts.** *[Notifications Page / Notification Center]*
- **Unread notifications are highlighted. Notifications automatically update to read, and the highlight is removed once clicked.** *[Notifications Page]*

## Documents Link
- **Functional Requirements Document** - [https://cebuinstituteoftechnology-my.sharepoint.com/:b:/g/personal/mathlee_biacolo_cit_edu/EQkl7GExwtdLj6NagGnM-uMBoQxGu4KhcKXVUXqQKzx3PQ?e=4zhwcD](https://cebuinstituteoftechnology-my.sharepoint.com/:w:/g/personal/mathlee_biacolo_cit_edu/EY2RvuHGkBpIniwKt_VxC80BF1ppnafqZr7pB4tuzL8lgw?e=hbYGpn)
- **Gantt Chart** - [https://cebuinstituteoftechnology-my.sharepoint.com/:x:/g/personal/mathlee_biacolo_cit_edu/EfKybpc0szZFo-HltRaQEhQBlNUPJrhNLKNTS-dbVxQ5rg?e=jhDcvw](https://cebuinstituteoftechnology-my.sharepoint.com/:x:/g/personal/mathlee_biacolo_cit_edu/EaftggmRtAlJtaOEl_HQCV0BsWGd86L-pcNUkuhiZlvezw?e=aPP9fi)
- **System ERD** - https://cebuinstituteoftechnology-my.sharepoint.com/:i:/g/personal/mathlee_biacolo_cit_edu/ETKLOu__3xdOrdkWqURaXLkBgQ0LObOJW2eweg-Bhfj8Rg?e=D5Pftg
- **UIUX Figma** - https://www.figma.com/design/KxtKGC2RcJdpSmID1ovZs9/Item-Exchange-Platform---Web-Design?node-id=0-1&t=3pNSQjHxgsga2Stx-1

  

## Technologies Used

  

- Django (Python web framework)

  

## Getting Started

  

**1. Clone the repository:**

  

```bash

git  clone  https://github.com/MasuRii/ItemExchangeApplication.git
