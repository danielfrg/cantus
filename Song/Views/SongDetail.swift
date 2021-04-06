//
//  SongDetail.swift
//  Cantus
//
//  Created by Daniel Rodriguez on 4/5/21.
//

import SwiftUI
import AVKit

struct SongDetail: View {
    var song: Song
    
    var bombSoundEffect: AVAudioPlayer?
    
//    @State private var backgroundSound: Sound?
    @State var audioPlayer: AVAudioPlayer!
    
    var body: some View {
        ZStack {
            VStack {
                Text(song.name).font(.system(size: 45)).font(.largeTitle)
                HStack {
                    Spacer()
                    Button(action: {
                        self.audioPlayer.play()
                    }) {
                        Image(systemName: "play.circle.fill").resizable()
                            .frame(width: 50, height: 50)
                            .aspectRatio(contentMode: .fit)
                    }
                    Spacer()
                    Button(action: {
                        self.audioPlayer.pause()
                    }) {
                        Image(systemName: "pause.circle.fill").resizable()
                            .frame(width: 50, height: 50)
                            .aspectRatio(contentMode: .fit)
                    }
                    Spacer()
                }
            }
        }
        .onAppear {
            let sound = Bundle.main.path(forResource: song.source, ofType: "mp3")
            if sound != nil {
                self.audioPlayer = try! AVAudioPlayer(contentsOf: URL(fileURLWithPath: sound!))
            }
        }

    }
    
//    private func fetch() {
//        if let pianoUrl = Bundle.main.url(forResource: song.source, withExtension: "wav") {
//            backgroundSound = Sound(url: pianoUrl)
//            backgroundSound?.volume = 0.8
//            backgroundSound?.prepare()
//        }
//    }
}

struct SongDetail_Previews: PreviewProvider {
    static var previews: some View {
        SongDetail(song: songs[0])
    }
}
