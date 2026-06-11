function Landing() {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');

    function handleClaim() {
        if (username.trim()) {
            navigate(`/register?username=${username}`);
        }
    }
    return (
        <div className={styles.page}>
            <nav className={styles.nav}>
                <div className={styles.logo}>luckI<span className={styles.logoAccent}>.me</span>
                </div>
                <div className={styles.navLinks}>
                    <a href="#">HELP</a>
                    <a href="#">PRICING</a>
                    <a href="#">DISCORD</a>
                    <a href="#">LEADERBOARD</a>
                </div>
                <div className={styles.navRight}>
                    <button className={styles.btnGhost} onClick={() => navigate('/login')}>
                        Login
                    </button>
                    <button className={styles.btnPrimary} onClick={() => navigate('/register')}>
                        Sign Up
                    </button>
                </div>   
            </nav>

            <section className={styles.hero}>
              <div className={styles.heroGlow} />
              <div className={styles.eyebrow}>Built for creators</div>
              <h1 className={styles.heroTitle}>A profile that says it all,<br /><span className={styles.grad}>right here</span></h1>
              <p className={styles.heroSub}> Your dev portfolio, business profile, or social ecosystem... one clean link to show who you are </p>
            
              <div className={styles.claimBar}>
                <span className={styles.claimPrefix}>luckI.me</span>
                <Input
                    className={styles.claimInput}
                    type="text"
                    placeholder="yourname"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <button className= {styles.claimBtn} onClick={handleClaim}>CLAIM NOW</button>
              </div>
              <p className={styles.heroNote}> Free forever.</p>
            </section>

          <div className={styles.stats}>
            <div className={styles.stat}>
              <div className={styles.statNum}>48K+</div>
              <div className={styles.statLbl}>Portfolios created</div>
            </div>
            <div className={styles.stat}>
              <div className={styles.statNum}>2.1M+</div>
              <div className={styles.statLbl}>Profile views</div>
            </div>
            <div className={styles.stat}>
              <div className={styles.statNum}>120K+</div>
              <div className={styles.statLbl}>Projects showcased</div>
            </div>
            <div className={styles.stat}>
              <div className={styles.statNum}>Free</div>
              <div className={styles.statLbl}>To get started</div>
            </div>
          </div>

          <section className={styles.features}>
           <div className={styles.featuresEyebrow}>Why Lucki</div>
           <h2 className={styles.featuresTitle}>Everything in one place</h2>
           <div className={styles.featuresGrid}>
            {[
              { icon: '⌨️', title: 'Project showcase', desc: 'Display your work with live links, GitHub repos, tech stacks and status labels.' },
              { icon: '🔗', title: 'Social links hub', desc: 'GitHub, LinkedIn, Instagram, X and more — all linked from one page.' },
              { icon: '🏢', title: 'Business profiles', desc: 'Perfect for startups — showcase your team, services and contact info.' },
              { icon: '📊', title: 'Profile analytics', desc: 'See who is visiting your page, where they are from and what they click.' },
              { icon: '🎨', title: 'Full customization', desc: 'Custom themes, fonts and layouts — make your page yours.' },
              { icon: '🔒', title: 'Private & secure', desc: 'No ads. No trackers. Just your work presented cleanly.' },
            ].map((f) => (
              <div key={f.title} className={styles.feat}>
                <div className={styles.featIcon}>{f.icon}</div>
                <div className={styles.featTitle}>{f.title}</div>
                <div className={styles.featDesc}>{f.desc}</div>
              </div>
            ))}
          </div>
        </section>

        <div className={styles.claimBanner}>
          <h2>Claim your profile today.</h2>
          <p>Join thousands of developers and businesses already on Lucki.</p>
          <div className={styles.claimBar}>
            <span className={styles.claimPrefix}>lucki.me/</span>
            <input
              className={styles.claimInput}
              type="text"
              placeholder="yourname"
            />
            <button className={styles.claimBtn}>Claim Now</button>
          </div>
        </div>
  
        <footer className={styles.footer}>
          <div>
            <div className={styles.logo}>lucki<span className={styles.logoAccent}>.me</span></div>
            <div className={styles.footerTagline}>The portfolio platform for<br />developers and businesses.</div>
          </div>
          <div className={styles.footerCol}>
            <h4>General</h4>
            <a href="#">Login</a>
            <a href="#">Sign up</a>
            <a href="#">Pricing</a>
          </div>
          <div className={styles.footerCol}>
            <h4>Resources</h4>
            <a href="#">Help center</a>
            <a href="#">Changelog</a>
            <a href="#">Discord</a>
          </div>
          <div className={styles.footerCol}>
            <h4>Legal</h4>
            <a href="#">Terms of service</a>
            <a href="#">Privacy policy</a>
          </div>
        </footer>
        <div className={styles.footerCopy}>
          Copyright © 2026 Lucki — All rights reserved.
        </div>

        
    </div>
    );
}

export default Landing;