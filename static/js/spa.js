// SPA JavaScript

let apiKey = "1c05c9b62d574400aa12613d42c083b8";

let request = new XMLHttpRequest();

request.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
     displayArticle(this.responseText);   
    }
}

function newArticle(i) {
    
    $("#marker").append(`
    
        <div class="row mt-3">
    
        <div class="col-md-3">
            <img class="img-fluid rounded" id="article_`+ i + `_img" src="" alt="">
        </div>
        
        <div class="col-md-9">
            <div class="row">
                <div class="col-md-3 text-uppercase">
                    <strong>Source</strong>
                </div>
                <div class="col-md-9" id="article_`+ i + `_source">
                
                </div>
            </div>
            <div class="row">
                <div class="col-md-3 text-uppercase">
                    <strong>Author</strong>
                </div>
                <div class="col-md-9" id="article_`+ i + `_author">
                </div>
            </div>
            <div class="row">
                <div class="col-md-3 text-uppercase">
                    <strong>Title</strong>
                </div>
                <div class="col-md-9" id="article_`+ i + `_title">
                    
                </div>
            </div>
            <div class="row">
                <div class="col-md-3 text-uppercase">
                    <strong>Description</strong>
                </div>
                <div class="col-md-9" id="article_`+ i + `_description">
                    
                </div>
            </div>
            <div class="row">
                <div class="col-md-3 text-uppercase">
                    <strong>ARTICLE</strong>
                </div>
                <div class="col-md-9" id="">
                    <a id="article_`+ i + `_url" href="" target="_blank"></a>
                </div>
            </div>
            <div class="row mb-3">
                <div class="col-md-3 text-uppercase">
                    <strong>Published at</strong>
                </div>
                <div class="col-md-9" id="article_`+ i + `_published_at">
                    
                </div>
            </div>
        </div>
    
    </div>
    
    <hr>
    `)
    
}

function writeArticle(i, article) {
    
    $("#article_" + i + "_img").attr("src", article["urlToImage"]);
    $("#article_" + i + "_url").attr("href", article["url"]);
    $("#article_" + i + "_source").text(article["source"]["name"]);
    $("#article_" + i + "_author").text(article["author"]);
    $("#article_" + i + "_title").text(article["title"]);
    $("#article_" + i + "_description").text(article["description"]);
    $("#article_" + i + "_url").text("READ FULL ARTICLE");
    // $("#article_" + i + "_url").text(article["url"]);
    $("#article_" + i + "_content").text(article["content"]);
    $("#article_" + i + "_published_at").text(article["publishedAt"]);
    
}

function displayArticle(apiData) {
    
    $("#marker").empty();
    
    let newsData = JSON.parse(apiData);
    let articlesArray = newsData["articles"];
    
    for (i=0; i< articlesArray.length; i++) {
        
        newArticle(i);
        writeArticle(i, articlesArray[i]);
    
    };
    
}

function submitSearch() {
    
    let query           = $("#searchbar").val();
    let radioSortBy     = $("input[name='sortBy']:checked").val();
    let radioLanguage   = $("input[name='language']:checked").val();
    let yesterday       = new Date(Date.now() - 86400000); // 24 * 60 * 60 * 1000
        yesterday       = yesterday.getFullYear() + '-' + (yesterday.getMonth() + 1) + '-' + yesterday.getDate() 
    
    request.open("GET", "https://newsapi.org/v2/everything?q=("  
                                    + query + ")" 
                                    + "&from="     + yesterday
                                    + "&language=" + radioLanguage
                                    + "&sortBy="   + radioSortBy
                                    + "&apiKey="   + apiKey
    );
    
    request.send();
    
    // request.onreadystatechange = function () {
    //     if (this.readyState == 4 && this.status == 200) {
    //         displayArticle(this.responseText);   
    //     }
    // }
    
}

// Link "Enter" key to button clic 
$(document).ready(function() {
    
    $("#searchbar").keyup(function(event) {
        if (event.keyCode === 13) { 
            $("#submit").click();
        }
    });
    
});


// request.open("GET", "https://newsapi.org/v2/everything?q=(Cybersecurity OR infosec)&from=2018-10-16&language=en&sortBy=popularity&apiKey=1c05c9b62d574400aa12613d42c083b8");
// request.open("GET", "https://api.mlab.com/api/1/databases/github-tweets/collections/CyberSecurity?apiKey=BJVr32yUrNipqBoA69TdUgrld3EYXLRA");
// request.open("GET", "https://api.openweathermap.org/data/2.5/weather?q=Dublin&APPID=6ebea87dfc131fd5402906ce4b098ab8");


// request.send();