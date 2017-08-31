import org.ansj.domain.Result;
import org.ansj.domain.Term;
import org.ansj.splitWord.analysis.ToAnalysis;
import java.util.*;
import java.io.*;


public class AnsjStatisticFre {
    private List<File> fileList = new ArrayList<File>();
    public int GetFileSize() {
      return this.fileList.size();
    }
    public int Init(String filePath) {
      //遍历文件夹
      File dir = new File(filePath);
      File[] files = dir.listFiles(); // 该文件目录下文件全部放入数组
      if (files != null) {
        for (int i = 0; i < files.length; i++) {
          String fileName = files[i].getName();
          if (files[i].isDirectory()) { // 判断是文件还是文件夹
            this.Init(files[i].getAbsolutePath()); // 获取文件绝对路径
          } else { // 判断是否是文件
            if (files[i] != null) {
              fileList.add(files[i]);
            }
          }
        }
        return 1;
      }
      return 0;
    }

    //分词
    public void start() {
        //只关注这些词性的词
        Set<String> expectedNature = new HashSet<String>() {{
            add("n");add("v");add("vd");add("vn");add("vf");
            add("vx");add("vi");add("vl");add("vg");
            add("nt");add("nz");add("nw");add("nl");
            add("ng");add("userDefine");add("wh");
        }};

        String str = "洁面仪配合洁面深层清洁毛孔 清洁鼻孔面膜碎觉使劲挤才能出一点点皱纹!!!!!!!!!!!!!";
        Result result = ToAnalysis.parse(str); //分词结果的一个封装，主要是一个List<Term>的terms
        System.out.println(result.getTerms());

        List<Term> terms = result.getTerms(); //拿到terms
        System.out.println(terms.size());

        for(int i=0; i<terms.size(); i++) {
            String word = terms.get(i).getName(); //拿到词
            String natureStr = terms.get(i).getNatureStr(); //拿到词性
            if(expectedNature.contains(natureStr)) {
                System.out.println(word + ":" + natureStr);
            }
        }
    }

    public static void main(String[] args) {
        AnsjStatisticFre fa = new AnsjStatisticFre();
        String file_path = "./";
        if (fa.Init(file_path) < 1) {
          System.out.println("init error " + file_path);
        }
        else {
          System.out.printf("file list len %d\n", fa.GetFileSize());
        }
        fa.start();
    }
}
