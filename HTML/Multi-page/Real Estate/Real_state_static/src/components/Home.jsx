import Logo from '../assets/Icons/Logo.svg'
// import Manrope from '../assets/Fonts/Manrope.ttf'
import mainBackground from '../assets/Photos/mainBackground.png'



const Home = () => {

  return (
    <div className=''>
      <header className=' w-full h-[100vh] bg-white flex flex-col  items-center pt-2 bg-cover bg-center bg-no-repeat ' style={{ backgroundImage: `url(${mainBackground})` }}>
      <nav className='w-5/6  flex justify-evenly space-x-20 border-b-2 border-blue-500 '>
        <img className=' size-20' src={Logo} alt="logo img" />
        {/* nav link */}
        <ul className='w-2/4 flex justify-evenly  items-center ml-20 text-white '>
          <li><a href="#">Location</a></li>
          <li><a href="#">Blogs</a></li>
          <li><a href="#">Testimonial</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>

      <div className='w-2/3 flex-col justify-start mt-20 space-y-4 '>
        <h1 className=' text-6xl font-bold'>Home That Makes <br /> You Living Life!</h1>
        <p>
          Are you looking for amazing Real estate? Don't worry we got it for you
        </p>
        <button>Learn More</button>
      </div>
    </header>
    </div>
  )
}

export default Home