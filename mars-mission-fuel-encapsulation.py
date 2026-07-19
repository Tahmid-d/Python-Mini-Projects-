class RocketEngine : 
    def __init__ (self,rocket_name,fuel_level) : 
        self.rocket_name = rocket_name 
        self.__fuel_level = fuel_level # private variable 
    def get_fuel_level (self) :## create getter method to "see the data" not change
        print(f"The rocket name is:{self.rocket_name}.{self.rocket_name} fuel level is:{self.__fuel_level}\n") 
        return self.__fuel_level ## use return
    def set_fuel_level (self,new_fuel_level) : ## create setter method to "change the data" but used condition (if-else) 
        if new_fuel_level >= 0 and new_fuel_level <= 100 : ## validation check
            self.__fuel_level = new_fuel_level
        else : 
            print(f"System Warning:Invalid fuel level! Engine lock engaged.Fuel level must 0% to 100% \n") 
        print(f"The rocket name is:{self.rocket_name}.{self.rocket_name} fuel level is:{self.__fuel_level} \n") 
## ## 🚀 STEP 1: রকেট অবজেক্ট তৈরি (Creating Rocket Instances)
## ক্লাসের ব্লুপ্রিন্ট (Blueprint) ব্যবহার করে ৪টি আলাদা রকেটের বাস্তব অস্তিত্ব (Objects) তৈরি করা হলো।
## ব্র্যাকেটের ভেতরের মানগুলো সরাসরি কনস্ট্রাক্টরে (__init__) গিয়ে রকেটের নাম ও শুরুর ফুয়েল সেট করছে। 
rocket_1=RocketEngine ("Are Space",80)
rocket_2=RocketEngine ("Flyspace",90)
rocket_3=RocketEngine ("neptune",92) 
rocket_4=RocketEngine ("Eurenape",77) 
## ## 🔒 STEP 2: এনক্যাপসুলেশন ও সিকিউরিটি গার্ড টেস্ট (Testing Security & Methods)
## এই জোনে আমরা গেটার (Getter) ও সেটার (Setter) মেথডগুলো কল করে রকেটের ফুয়েল লেভেল কন্ট্রোল করছি।
## এখানে সঠিক ডাটার পাশাপাশি ভুল ডাটা (যেমন: -২৩) পুশ করে পরীক্ষা করা হচ্ছে যে আমাদের সিকিউরিটি গার্ড ঠিকমতো হ্যাকিং আটকাতে পারছে কি না।
rocket_1 .set_fuel_level(87) 
rocket_2.set_fuel_level(90)
rocket_3. set_fuel_level(-23) 
rocket_4.get_fuel_level() 