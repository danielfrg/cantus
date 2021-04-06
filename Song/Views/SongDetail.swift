//
//  SongDetail.swift
//  Cantus
//
//  Created by Daniel Rodriguez on 4/5/21.
//

import SwiftUI
import SwiftySound
import AVFoundation

struct SongDetail: View {
    var song: Song
    
    var bombSoundEffect: AVAudioPlayer?
    
    @State private var backgroundSound: Sound?
    
    var body: some View {
        Text(song.name)
            .onAppear(perform: fetch)
    }
    
    private func fetch() {
        if let pianoUrl = Bundle.main.url(forResource: song.source, withExtension: "wav") {
            backgroundSound = Sound(url: pianoUrl)
            backgroundSound?.volume = 0.8
            backgroundSound?.prepare()
        }
    }
}

struct SongDetail_Previews: PreviewProvider {
    static var previews: some View {
        SongDetail(song: songs[0])
    }
}
