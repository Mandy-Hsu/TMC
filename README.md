# TMC

The main idea of this script is to autmate Google search when it comes to finding
online grant portals.

Currently there are two main parts of this program:
  Input: accepts a text file, delimited only by single space. For example:
    Google CA
    Citi NY
    
  So far the assumption is that the first string literal will be a company name and the second will be location.
  
  
  Output: exports a text file in the same root file as the input text file. It will run and store three urls for
  each company entry. THe result will look somewhat like this:
  
  Results for Google
    https://www.wholewhale.com/tips/how-to-apply-for-google-ad-grant/
    https://www.philanthropy.com/article/Podcast-Google-s-Foundation/244657
    https://www.geek.com/google/google-staff-do-community-service-1265717/

  Results for Citi
    https://www.citigroup.com/citi/foundation/about/grant-guidelines.htm
    https://www.citigroup.com/citi/foundation/
    https://www.citigroup.com/citi/citizen/community/
    
  The result is produced by running the company names with the three keywords: 
    ["grant application", "giving back", "community service"]
