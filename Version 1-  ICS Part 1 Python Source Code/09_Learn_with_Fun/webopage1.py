from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Springfield High School</title>
        <style>
            /* Reset */
            * {
                margin: 0; padding: 0; box-sizing: border-box;
            }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #f0f4f8;
                color: #333;
                line-height: 1.6;
            }
            header {
                background: linear-gradient(135deg, #4a90e2, #50e3c2);
                color: white;
                padding-bottom: 50px;
            }
            nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 20px 50px;
            }
            .logo {
                font-size: 1.8rem;
                font-weight: 700;
            }
            nav ul {
                list-style: none;
                display: flex;
                gap: 25px;
            }
            nav ul li a {
                color: white;
                text-decoration: none;
                font-weight: 600;
                transition: color 0.3s ease;
            }
            nav ul li a:hover {
                color: #ffd700;
            }
            .hero {
                text-align: center;
                padding: 60px 20px 40px 20px;
            }
            .hero h1 {
                font-size: 3rem;
                margin-bottom: 15px;
            }
            .hero p {
                font-size: 1.5rem;
                margin-bottom: 30px;
                font-weight: 400;
            }
            .btn {
                background: #ffd700;
                color: #333;
                padding: 12px 35px;
                border: none;
                border-radius: 50px;
                font-weight: 700;
                font-size: 1.1rem;
                cursor: pointer;
                text-decoration: none;
                transition: background 0.3s ease;
            }
            .btn:hover {
                background: #e6c200;
            }
            section {
                max-width: 1100px;
                margin: 40px auto;
                padding: 0 20px;
            }
            .about, .programs {
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                margin-bottom: 40px;
                text-align: center;
            }
            .about h2, .programs h2 {
                margin-bottom: 20px;
                color: #4a90e2;
            }
            .cards {
                display: flex;
                justify-content: center;
                gap: 30px;
                flex-wrap: wrap;
            }
            .card {
                background: #50e3c2;
                color: white;
                padding: 25px 20px;
                border-radius: 12px;
                flex: 1 1 250px;
                box-shadow: 0 6px 15px rgba(0,0,0,0.1);
                transition: transform 0.3s ease;
            }
            .card:hover {
                transform: translateY(-10px);
            }
            .card h3 {
                margin-bottom: 15px;
            }
            footer {
                background: #222;
                color: #bbb;
                text-align: center;
                padding: 15px 10px;
                font-size: 0.9rem;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <header>
            <nav>
                <div class="logo">Springfield High</div>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Admissions</a></li>
                    <li><a href="#">Academics</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </nav>
            <div class="hero">
                <h1>Welcome to Springfield High School</h1>
                <p>Where Learning Meets Excellence</p>
                <a href="#" class="btn">Learn More</a>
            </div>
        </header>

        <section class="about">
            <h2>About Our School</h2>
            <p>
                Springfield High School has been providing quality education since 1985. 
                Our dedicated faculty and modern facilities create an environment where students can thrive academically and personally.
            </p>
        </section>

        <section class="programs">
            <h2>Our Programs</h2>
            <div class="cards">
                <div class="card">
                    <h3>Science & Technology</h3>
                    <p>Explore innovation with our advanced STEM curriculum and state-of-the-art labs.</p>
                </div>
                <div class="card">
                    <h3>Arts & Humanities</h3>
                    <p>Nurture creativity through music, drama, literature, and visual arts programs.</p>
                </div>
                <div class="card">
                    <h3>Sports & Fitness</h3>
                    <p>Encourage teamwork and fitness with diverse sports teams and wellness activities.</p>
                </div>
            </div>
        </section>

        <footer>
            <p>&copy; 2025 Springfield High School | Contact: info@springfieldhigh.edu | Phone: (123) 456-7890</p>
        </footer>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
