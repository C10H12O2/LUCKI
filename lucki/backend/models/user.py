from backend.app import db, ma
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    
    #Profile fields
    display_name = db.Column(db.String(100))
    tagline = db.Column(db.String(200))
    avatar_url = db.Column(db.String(300))

    #Social links
    snapchat = db.Column(db.String(200))
    youtube = db.Column(db.String(200))
    discord = db.Column(db.String(200))
    spotify = db.Column(db.String(200))
    instagram = db.Column(db.String(200))
    twitter = db.Column(db.String(200))
    tiktok = db.Column(db.String(200))
    telegram = db.Column(db.String(200))
    soundcloud = db.Column(db.String(200))
    paypal = db.Column(db.String(200))
    github = db.Column(db.String(200))
    roblox = db.Column(db.String(200))
    cashapp = db.Column(db.String(200))
    venmo = db.Column(db.String(200))
    playstation = db.Column(db.String(200))
    xbox = db.Column(db.String(200))
    apple_music = db.Column(db.String(200))
    gitlab = db.Column(db.String(200))
    twitch = db.Column(db.String(200))
    reddit = db.Column(db.String(200))
    vk = db.Column(db.String(200))
    telonym = db.Column(db.String(200))
    bluesky = db.Column(db.String(200))
    namemc = db.Column(db.String(200))
    linkedin = db.Column(db.String(200))
    steam = db.Column(db.String(200))
    kick = db.Column(db.String(200))
    pinterest = db.Column(db.String(200))
    lastfm = db.Column(db.String(200))
    payhip = db.Column(db.String(200))
    facebook = db.Column(db.String(200))
    buy_me_a_coffee = db.Column(db.String(200))
    kofi = db.Column(db.String(200))
    threads = db.Column(db.String(200))
    patreon = db.Column(db.String(200))
    signal = db.Column(db.String(200))
    bitcoin = db.Column(db.String(200))
    ethereum = db.Column(db.String(200))
    litecoin = db.Column(db.String(200))
    solana = db.Column(db.String(200))
    xrp = db.Column(db.String(200))
    monero = db.Column(db.String(200))
    email = db.Column(db.String(200))
    Add_custom_url = db.Column(db.String(200))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<User {self.username}>'
    
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('password_hash',)
