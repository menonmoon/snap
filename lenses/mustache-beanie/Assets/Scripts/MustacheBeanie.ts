/**
 * Mustache + beanie face lens.
 *
 * Imitates the accessory-style face lenses in the Lens+ top chart (for example
 * "mustache + beanie" and "mustache + tattoos"). Two PNG overlays are anchored
 * to the tracked face: a mustache at the mouth and a beanie on the forehead.
 *
 * Textures, sizes and the face index are inputs, so they can be tuned in the
 * Inspector without editing code.
 */
@component
export class MustacheBeanie extends BaseScriptComponent {
  @input
  mustacheTexture: Texture;

  @input
  beanieTexture: Texture;

  @input
  mustacheSize: number = 0.35;

  @input
  beanieSize: number = 1.2;

  @input
  faceIndex: number = 0;

  onAwake() {
    this.createEvent("OnStartEvent").bind(() => this.build());
  }

  private build() {
    this.addOverlay("Mustache", this.mustacheTexture, AttachmentPointType.MouthCenter, this.mustacheSize);
    this.addOverlay("Beanie", this.beanieTexture, AttachmentPointType.Forehead, this.beanieSize);
  }

  private addOverlay(name: string, texture: Texture, anchor: AttachmentPointType, size: number) {
    if (!texture) {
      print(`MustacheBeanie: no texture assigned for ${name}`);
      return;
    }

    // The anchor follows a point on the face. The overlay is its child, so it
    // inherits that position and moves with the head.
    const anchorObject = global.scene.createSceneObject(`${name} Anchor`);
    anchorObject.setParent(this.sceneObject);
    const head = anchorObject.createComponent("Component.Head") as Head;
    head.faceIndex = this.faceIndex;
    head.setAttachmentPointType(anchor);

    const overlay = global.scene.createSceneObject(name);
    overlay.setParent(anchorObject);
    const image = overlay.createComponent("Component.Image") as Image;
    image.mainPass.baseTex = texture;
    overlay.getTransform().setLocalScale(new vec3(size, size, size));
  }
}
