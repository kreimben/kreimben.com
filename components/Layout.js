import Head from 'next/head'

import Menu from '../components/Menu';

export default function Layout(props) {
    return (
        <div>
            <Head>
                <title> {props.title} </title>
            </Head>

            <Header isHome={props.isHome} />

            <Menu />

            <main>
                {props.children}
            </main>

            <footer className="shadow-outter h-auto py-2 flex justify-center items-center bg-gray-300">
                <div className="flex-row justify-center">
                    <div className="mx-auto w-auto py-12 flex justify-center space-x-8">
                        <a className="" href="https://paypal.me/kreimben" target="_blank">
                            <img src="paypal_favicon.png" className="bg-transparent w-16 h-16" />
                        </a>
                        <a className="" href="https://github.com/kreimben" target="_blank">
                            <img src="github_favicon.png" className="bg-transparent w-16 h-16" />
                        </a>
                        <a className="" href="mailto:aksidion@kreimben.com">
                            <img src="mail_favicon.png" className="bg-transparent w-16 h-16" />
                        </a>
                    </div>

                    <p className="font-mono text-sm mb-8">Copyright(C) 2019 - 2020. Aksidion Kreimben. All right reserved.</p>
                </div>
            </footer>

        </div>
    )
}

function Header(props) {
    if (props.isHome) {
        return (
            <HomeHeader />
        );
    } else {
        return (
            <JustHeader />
        );
    }
}

function HomeHeader(props) {
    return (
        <div>
            <header className="text-center bg-fixed bg-center h-screen items-center">
                <div className="flex justify-center pt-8 pb-8">
                    <img src="/images/kreimben_memoji.jpeg" className="rounded-full flex justify-center w-40 h-40 shadow-2xl"></img>
                </div>
                <p className="text-2xl font-light font-mono bg-white bg-opacity-50 rounded-lg px-3 py-2 inline-block">Kreimben.com, Indie developer's website</p>
            </header>
            <style jsx>
                {`
                
                header {
                    background-image: url('/images/backgroundImage.jpg');
                }
                
                `}
            </style>
        </div>
    );
}

function JustHeader(props) {
    return (
        <div>
            <header className="text-center bg-cover bg-center h-auto items-center">
                <div className="flex justify-center py-8">
                    <img src="/images/kreimben_memoji.jpeg" className="rounded-full flex justify-center w-40 h-40 shadow-2xl"></img>
                </div>
                <p className="text-2xl font-light font-mono bg-white bg-opacity-50 rounded-lg px-3 py-2 mb-8 inline-block">Kreimben.com, Indie developer's website</p>
            </header>
            <style jsx>
                {`
                
                header {
                    background-image: url('/images/backgroundImage.jpg');
                }
                
                `}
            </style>
        </div>
    );
}