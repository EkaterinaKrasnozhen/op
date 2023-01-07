package lec4.Ex3;

public class Program {
    public static void main(String[] args) {
        Repository<AudioContent> audioStorage = new Repository<>("audioStorage");
        audioStorage.add(new AudioContent("audioTrack1.mp3"));
        audioStorage.add(new AudioContent("audioTrack2.wma"));

        for (int index = 0; index < audioStorage.count(); index++) {
            System.out.println(audioStorage.get(index));
        }

        Repository<VideoContent> videoStorage = new Repository<>("videoStorage");
        videoStorage.add(new VideoContent("Film1.wmv"));
        videoStorage.add(new VideoContent("Film2.3gp"));
       
        Repository<VideoContent> videoStorage2 = new Repository<>("videoStorage2");
        videoStorage2.add(new VideoContent("Film3.wmv"));
        videoStorage2.add(new VideoContent("Film4.3gp"));
        

        for (int index = 0; index < videoStorage.count(); index++) {
            System.out.println(videoStorage.get(index));
        }

        for (Content el : audioStorage) {
            System.out.println(el);
        }

        for (Content element : videoStorage) {
            System.out.println(element);
        }

        System.out.println("-----");
        videoStorage.merge(videoStorage2);
        for (Content elem : videoStorage) {
            System.out.println(elem);
        }
    }
}
