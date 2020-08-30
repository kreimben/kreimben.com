import Head from 'next/head'

import Menu from '../components/Menu';

export default function Layout(props) {
    return (
        <div>
            <Head>
                <title> {props.title} </title>
            </Head>

            <header className="text-center bg-gradient-to-t from-teal-400 to-indigo-500">
                    <div className="w-full flex justify-center py-8">
                        <img src="/images/kreimben_memoji.jpeg" className="rounded-full flex justify-center w-40 h-40 shadow-2xl"></img>
                    </div>
                    <p className="text-2xl font-light font-mono pb-6">Kreimben.com, Indie developer's website</p>
            </header>

            <Menu />

            <main>
                {props.children}
            </main>

        </div>
    )
}